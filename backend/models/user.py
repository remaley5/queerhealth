from . import db
from . import utcnow
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_digest = db.Column(db.String(255), nullable=False)

    user_provider = db.relationship("User_Provider", back_populates="user")

    @property
    def password(self):
        raise AttributeError('Password not readable.')

    @password.setter
    def password(self, password):
        self.password_digest = generate_password_hash(password)

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter(User.email == email).scalar()
        if user is None:
            return False, user
        return check_password_hash(user.password_digest, password), user


class Healthcare_Title(db.Model):
    __tablename__ = 'health_title'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)

    health_provider = db.relationship("Health_Provider", back_populates="title")


class State(db.Model):
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(30), nullable=False, unique=True)

    health_provider = db.relationship("Health_Provider", back_populates="state")


class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(40), nullable=False, unique=True)

    health_provider = db.relationship("Health_Provider", back_populates="city")


class Zip_Code(db.Model):
    __tablename__ = 'zip_codes'

    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Integer, nullable=False, unique=True)

    health_provider = db.relationship("Health_Provider", back_populates="zip_code")

class Health_Provider(db.Model):
    __tablename__ = 'health_providers'

    id = db.Column(db.Integer, primary_key=True)
    title_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=True)
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    zip_code_id = db.Column(db.Integer, db.ForeignKey('zip_codes.id'), nullable=False)

    state = db.relationship("State", back_populates="health_providers")
    city = db.relationship("City", back_populates="health_providers")
    zip_code = db.relationship("Zip_Code", back_populates="health_providers")
    title = db.relationship("Healthcare_Title", back_populates="health_provider")
    reviews = db.relationship("Review", back_populates="health_provider")
    services = db.relationship("Provider_Services", back_populates="health_provider")
    specialties = db.relationship("Provider_Specialties", back_populates="health_provider")

    user_provider = db.relationship("User_Provider", back_populates="health_provider")


class User_Provider(db.Model):
    __tablename__ = 'user_providers'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    health_provider_id = db.Column(db.Integer, db.ForeignKey('health_providers.id'), nullable=False)

    health_provider = db.relationship("Health_Provider", back_populates="user_provider")
    user = db.relationship("User", back_populates="user_provider")


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(40), nullable=False, unique=True)

    review_tags = db.relationship("Tag", back_populates="tag")


class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    health_provider_id = db.Column(db.Integer, db.ForeignKey('health_providers.id'), nullable=False)
    good = db.Column(db.Text)
    bad = db.Column(db.Text)
    rating = db.Column(db.Integer, nullable=False)

    review_tags = db.relationship("Review_Tag", back_populates="review")
    health_provider = db.relationship("Health_Provider", back_populates="reviews")


class Review_Tag(db.Model):
    __tablename__ = 'review_tags'

    id = db.Column(db.Integer, primary_key=True)
    quality = db.Column(db.Boolean, nullable=False)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)

    review = db.relationship("Review", back_populates="review_tags")
    tag = db.relationship("Tag", back_populates="review_tags")


class Specialties(db.Model):
    __tablename__ = "specialties"

    id = db.Column(db.Integer, primary_key=True)
    specialty = db.Column(db.String(100), nullable=False)

    provider_specialties = db.relationship("Provider_Specialties", back_populates="specialty")


class Provider_Specialties(db.Model):
    __tablename__ = "provider_specialties"

    id = db.Column(db.Integer, primary_key=True)
    specialty_id = db.Column(db.Integer, db.ForeignKey('specialties.id'), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('health_providers.id'), nullable=False)

    specialty = db.relationship("Specialties", back_populates="provider_specialties")
    health_provider = db.relationship("Health_Provider", back_populates="")


class Service(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), nullable=False)

    provider_services = db.relationship("Provider_Services", back_populates="services")


class Provider_Servicess(db.Model):
    __tablename__ = "provider_services"

    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('health_providers.id'), nullable=False)

    services = db.relationship("Service", back_populates="provider_services")
    health_provider = db.relationship("Health_Provider", back_populates="services")
