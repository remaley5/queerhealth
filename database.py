from backend.models.user import (User, Gender, Race, Sexuality, Realtionship_Preference,
                            Healthcare_Title, State, City, Zip_Code, Health_Provider,
                            User_Provider, Tag, Review, Review_Tag, Specialties, Provider_Specialties, Service, Provider_Services)
from backend import app, db
from dotenv import load_dotenv

load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()

    users = [
        User(first_name='demo',
             last_name='demo',
             email='demo@aa.io',
             password='password',
             state_id=1,
             city_id=2,
             zip_code_id=1,
             sexuality_id=2,
             race_id=1,
             gender_id=4
             )
    ]

    locations = [
        State(state="New York"),
        State(state="Oregon"),
        City(city="Seattle"),
        City(city="New York"),
        Zip_Code(zip_code=10005)
    ]

    sexualities = [
        Sexuality(sexuality="Asexual"),
        Sexuality(sexuality="Bicurious"),
        Sexuality(sexuality="Bisexual"),
    ]

    genders = [
        Gender(gender="Cisgender"),
        Gender(gender="Non-Binary"),
        Gender(gender="Transgender"),
        Gender(gender="Gender Fluid"),
    ]

    races = [
        Race(race="White"),
        Race(race="African American"),
        Race(race="Asian"),
    ]

    hc_title = [
        Healthcare_Title(title="Doctor"),
        Healthcare_Title(title="Nurse"),
    ]

    hc_provs = [
        Health_Provider(
            title_id=1,
            first_name="Bob",
            last_name="Dylan",
            state_id=1,
            city_id=2,
            zip_code_id=1
        )
    ]

    rel_prefs = [
        Realtionship_Preference(
            user_id=1,
            sexuality_id=2
        )
    ]

    tags = [
        Tag(
            word="Compassionate"
        ),
        Tag(
            word="Timely"
        ),
        Tag(
            word="Arrogant"
        )
    ]

    reviews = [
        Review(
            health_provider_id=1,
            good="Compassionate and great bedside manner",
            bad="At times is arrogant",
            rating=8
        )
    ]

    review_tags = [
        Review_Tag(
            quality=True,
            review_id=1,
            tag_id=1
        ),
        Review_Tag(
            quality=False,
            review_id=1,
            tag_id=3
        )
    ]

    specialties = [
        Specialties(
            specialty="Eating Disorders"
        )
    ]

    services = [
        Service(
            service="Mental Health"
        )
    ]

    provider_specialties = [
        Provider_Services(
            service_id=1,
            provider_id=1
        )
    ]

    provider_services = [
        Provider_Specialties(
            specialty_id=1,
            provider_id=1
        )
    ]

    user_providers = [
        User_Provider(
            user_id=1,
            health_provider_id=1
        )
    ]
    for location in locations:
        db.session.add(location)

    for sexuality in sexualities:
        db.session.add(sexuality)

    for gender in genders:
        db.session.add(gender)

    for title in hc_title:
         db.session.add(title)

    for spec in specialties:
        db.session.add(spec)

    for tag in tags:
        db.session.add(tag)

    for service in services:
        db.session.add(service)

    for race in races:
        db.session.add(race)

    for user in users:
        db.session.add(user)

    for rel_pref in rel_prefs:
        db.session.add(rel_pref)

    for review in reviews:
        db.session.add(review)

    for tag in review_tags:
        db.session.add(tag)

    for hc_prov in hc_provs:
        db.session.add(hc_prov)

    for prov_special in provider_specialties:
        db.session.add(prov_special)

    for prov_service in provider_services:
        db.session.add(prov_service)

    for up in user_providers:
        db.session.add(up)


    db.session.commit()
