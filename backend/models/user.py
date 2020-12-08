from . import db
from . import utcnow
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class State(db.Model):
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(30), nullable=False, unique=True)

    health_providers = db.relationship("Health_Provider", back_populates="state")
    user = db.relationship("User", back_populates="state")


class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(40), nullable=False, unique=True)

    health_providers = db.relationship("Health_Provider", back_populates="city")
    user = db.relationship("User", back_populates="city")


class Zip_Code(db.Model):
    __tablename__ = 'zip_codes'

    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.Integer, nullable=False, unique=True)

    health_providers = db.relationship("Health_Provider", back_populates="zip_code")
    user = db.relationship("User", back_populates="zip_code")


class Gender(db.Model):
    __tablename__ = 'gender'

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(20), nullable=False)

    users = db.relationship("User_Gender", back_populates="gender")


class Race(db.Model):
    __tablename__ = 'race'

    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(20), nullable=False)

    user = db.relationship("User", back_populates="race")


class Sexuality(db.Model):
    __tablename__ = 'sexuality'

    id = db.Column(db.Integer, primary_key=True)
    sexuality = db.Column(db.String(20), nullable=False)

    """ relationship_pref not related to sexuality """

    user = db.relationship("User_Sexuality", back_populates="sexuality")


class Specialties(db.Model):
    __tablename__ = "specialties"

    id = db.Column(db.Integer, primary_key=True)
    specialty = db.Column(db.String(100), nullable=False)

    provider_specialties = db.relationship("Provider_Specialties", back_populates="specialty")


class Service(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), nullable=False)

    provider_services = db.relationship("Provider_Services", back_populates="services")

class Healthcare_Title(db.Model):
    __tablename__ = 'health_title'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)

    health_provider = db.relationship("Health_Provider", back_populates="title")


class Health_Provider(db.Model):
    __tablename__ = 'health_providers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=True)
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    zip_code_id = db.Column(db.Integer, db.ForeignKey('zip_codes.id'), nullable=False)
    title_id = db.Column(db.Integer, db.ForeignKey('health_title.id'), nullable=False)

    state = db.relationship("State", back_populates="health_providers")
    city = db.relationship("City", back_populates="health_providers")
    zip_code = db.relationship("Zip_Code", back_populates="health_providers")
    title = db.relationship("Healthcare_Title", back_populates="health_provider")
    reviews = db.relationship("Review", back_populates="health_provider")
    services = db.relationship("Provider_Services", back_populates="health_provider")
    specialties = db.relationship("Provider_Specialties", back_populates="health_provider")


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    """ took out first_name & last_name and added username """
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_digest = db.Column(db.String(255), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    zip_code_id = db.Column(db.Integer, db.ForeignKey('zip_codes.id'))
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'))

    """ Took out sexuality_id and made user_preference into user_sexuality
    so that one user can choose multiple sexualities
    same for gender and gender_id """
    sexuality = db.relationship("User_Sexuality", back_populates="user")
    gender = db.relationship("User_Gender", back_populates="user")

    race = db.relationship("Race", back_populates="user", cascade="all, delete")

    """ took out user_provider because that would be set up by who they review? """

    state = db.relationship("State", back_populates="user", cascade="all, delete")
    city = db.relationship("City", back_populates="user")
    zip_code = db.relationship("Zip_Code", back_populates="user")


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

    def safe_user(self):
        user = {
            'ids':self.id,
            'state':self.state.state,
            'city':self.city.city,
            'zip':self.zip_code.zip_code,
            'gender':self.gender.gender,
            'race':self.race.race,
        }
        return user

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(40), nullable=False, unique=True)

    review_tags = db.relationship("Review_Tag", back_populates="tag")

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


class Provider_Specialties(db.Model):
    __tablename__ = "provider_specialties"

    id = db.Column(db.Integer, primary_key=True)
    specialty_id = db.Column(db.Integer, db.ForeignKey('specialties.id'), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('health_providers.id'), nullable=False)

    specialty = db.relationship("Specialties", back_populates="provider_specialties")
    health_provider = db.relationship("Health_Provider", back_populates="")


class Provider_Services(db.Model):
    __tablename__ = "provider_services"

    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('health_providers.id'), nullable=False)

    services = db.relationship("Service", back_populates="provider_services")
    health_provider = db.relationship("Health_Provider", back_populates="services")


class User_Sexuality (db.Model):
    __tablename__ = 'user_sexuality'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    sexuality_id = db.Column(db.Integer, db.ForeignKey('sexualities.id'))

    user = db.relationship("User", back_populates="user_sexuality")
    sexuality =  db.relationship("Sexuality", back_populates="user_sexuality")

class User_Gender (db.Model):
    __tablename__ = 'user_gender'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    gender_id = db.Column(db.Integer, db.ForeignKey('genders.id'))

    user = db.relationship("User", back_populates="user_gender")
    gender =  db.relationship("Gender", back_populates="user_gender")
