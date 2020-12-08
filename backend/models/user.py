from . import db
from . import utcnow
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class State(db.Model):
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(30), nullable=False, unique=True)

    health_providers = db.relationship("Health_Provider", back_populates="states")
    users = db.relationship("User", back_populates="states")


class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(40), nullable=False, unique=True)

    health_providers = db.relationship("Health_Provider", back_populates="cities")
    users = db.relationship("User", back_populates="cities")


class Zip_Code(db.Model):
    __tablename__ = 'zip_codes'

    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.Integer, nullable=False, unique=True)

    health_providers = db.relationship("Health_Provider", back_populates="zip_codes")
    users = db.relationship("User", back_populates="zip_codes")


class Gender(db.Model):
    __tablename__ = 'genders'

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(20), nullable=False)

    user_genders = db.relationship("User_Gender", back_populates="genders")


class Race(db.Model):
    __tablename__ = 'races'

    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(20), nullable=False)

    users = db.relationship("User", back_populates="races")


class Sexuality(db.Model):
    __tablename__ = 'sexualities'

    id = db.Column(db.Integer, primary_key=True)
    sexuality = db.Column(db.String(20), nullable=False)

    """ relationship_pref not related to sexuality """

    user_sexualities = db.relationship("User_Sexuality", back_populates="sexualities")


class Specialty(db.Model):
    __tablename__ = "specialties"

    id = db.Column(db.Integer, primary_key=True)
    specialty = db.Column(db.String(100), nullable=False)

    provider_specialties = db.relationship("Provider_Specialty", back_populates="specialties")


class Service(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), nullable=False)

    provider_services = db.relationship("Provider_Services", back_populates="services")


class Healthcare_Title(db.Model):
    __tablename__ = 'health_titles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)

    health_providers = db.relationship("Health_Provider", back_populates="titles")


class Health_Provider(db.Model):
    __tablename__ = 'health_providers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=True)
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=True)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=True)
    zip_code_id = db.Column(db.Integer, db.ForeignKey('zip_codes.id'), nullable=True)
    title_id = db.Column(db.Integer, db.ForeignKey('health_titles.id'), nullable=False)

    states = db.relationship("State", back_populates="health_providers", cascade="all, delete")
    cities = db.relationship("City", back_populates="health_providers")
    zip_codes = db.relationship("Zip_Code", back_populates="health_providers")
    titles = db.relationship("Healthcare_Title", back_populates="health_providers")
    reviews = db.relationship("Review", back_populates="health_providers")
    services = db.relationship("Provider_Services", back_populates="health_providers")
    provider_specialties = db.relationship("Provider_Specialty", back_populates="health_providers")
    user_providers = db.relationship("User_Provider", back_populates="health_providers")


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
    race_id = db.Column(db.Integer, db.ForeignKey('races.id'))

    """ Took out sexuality_id and made user_preference into user_sexuality
    so that one user can choose multiple sexualities
    same for gender and gender_id """

    user_sexualities = db.relationship("User_Sexuality", back_populates="users")
    user_genders = db.relationship("User_Gender", back_populates="users")

    races = db.relationship("Race", back_populates="users", cascade="all, delete")
    user_providers = db.relationship("User_Provider", back_populates="users", cascade="all, delete")

    states = db.relationship("State", back_populates="users", cascade="all, delete")
    cities = db.relationship("City", back_populates="users")
    zip_codes = db.relationship("Zip_Code", back_populates="users")

    reviews = db.relationship("Review")


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

    review_tags = db.relationship("Review_Tag", back_populates="tags")

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    health_provider_id = db.Column(db.Integer, db.ForeignKey('health_providers.id'), nullable=False)
    good = db.Column(db.Text)
    bad = db.Column(db.Text)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    review_tags = db.relationship("Review_Tag", back_populates="reviews")
    health_providers = db.relationship("Health_Provider", back_populates="reviews")

    users = db.relationship("User", back_populates="reviews")


class Review_Tag(db.Model):
    __tablename__ = 'review_tags'

    id = db.Column(db.Integer, primary_key=True)
    quality = db.Column(db.Boolean, nullable=False)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)

    reviews = db.relationship("Review", back_populates="review_tags")
    tags = db.relationship("Tag", back_populates="review_tags")


class Provider_Specialty (db.Model):
    __tablename__ = "provider_specialties"

    id = db.Column(db.Integer, primary_key=True)
    specialty_id = db.Column(db.Integer, db.ForeignKey('specialties.id'), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('health_providers.id'), nullable=False)

    specialties = db.relationship("Specialty", back_populates="provider_specialties")
    health_providers = db.relationship("Health_Provider", back_populates="provider_specialties")


class Provider_Services(db.Model):
    __tablename__ = "provider_services"

    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('health_providers.id'), nullable=False)

    services = db.relationship("Service", back_populates="provider_services")
    health_providers = db.relationship("Health_Provider", back_populates="services")


class User_Sexuality (db.Model):
    __tablename__ = 'user_sexualities'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    sexuality_id = db.Column(db.Integer, db.ForeignKey('sexualities.id'))

    users = db.relationship("User", back_populates="user_sexualities")
    sexualities =  db.relationship("Sexuality", back_populates="user_sexualities")

class User_Gender (db.Model):
    __tablename__ = 'user_genders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    gender_id = db.Column(db.Integer, db.ForeignKey('genders.id'))

    users = db.relationship("User", back_populates="user_genders")
    genders =  db.relationship("Gender", back_populates="user_genders")

class User_Provider(db.Model):
    __tablename__ = 'user_providers'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    health_provider_id = db.Column(db.Integer, db.ForeignKey('health_providers.id'), nullable=False)

    health_providers = db.relationship("Health_Provider", back_populates="user_providers")
    users = db.relationship("User", back_populates="user_providers")
