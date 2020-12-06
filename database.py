from backend.models import (User, Gender, Race, Sexuality, Realtionship_Preference,
                            Healthcare_Title, State, City, Zip_Code, Health_Provider,
                            User_Provider, Tag, Review, Review_Tag, Specialties, Provider_Specialties, Service, Provider_Servicess)
from backend import app, db
from dotenv import load_dotenv

load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()

    users = [

        User(first_name='demo', last_name='demo', email='demo@aa.io',
                    password='password')
    ]

    locations = [

    ]

    sexualities = [

    ]

    genders = [

    ]

    hc_title = [

    ]

    hc_provs = [

    ]

    rel_prefs = [

    ]

    tags = [

    ]

    reviews = [

    ]

    review_tags = [

    ]

    Specialties = [

    ]

    services = [

    ]

    provider_specialties = [

    ]

    provider_services = [

    ]

    for location in locations:
        db.session.add(location)

    for sexuality in sexualities:
        db.session.add(sexuality)

    for gender in genders:
        db.session.add(gender)

    for race in races:
        db.session.add(race)

    for user in users:
        db.session.add(user)

    for rel_pref in rel_prefs:
        db.session.add(rel_pref)

    for title in hc_title:
         db.session.add(title)

    for spec in specialties:
        db.session.add(spec)

    for service in services:
        db.session.add(service)

    for tag in tags:
        db.session.add(tag)

    for hc_prov in hc_provs:
        db.session.add(hc_prov)

    for review in reviews:
        db.session.add(review)

    for tag in review_tags:
        db.session.add(tag)

    for prov_special in provider_specialties:
        db.session.add(prov_special)

    for prov_service in provider_services:
        db.session.add(prov_service)

    db.session.commit()
