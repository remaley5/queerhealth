from backend.models.user import (User, Gender, Race, Sexuality,
                            Healthcare_Title, State, City, Zip_Code, Health_Provider,
                             Tag, Review, Review_Tag, Specialties, Provider_Specialties, Service, Provider_Services)
from backend import app, db
from dotenv import load_dotenv

load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()

    users = [
        User(username='demo',
             email='demo@aa.io',
             password='password',
             state_id=1,
             city_id=2,
             zip_code_id=1,
             sexuality_id=2,
             race_id=1,
             gender_id=4
             ),
         User(username='mrlockin',
             email='demo@aa.io',
             password='password',
             state_id=1,
             city_id=2,
             zip_code_id=1,
             sexuality_id=2,
             race_id=1,
             gender_id=4
             ),
         User(username='pansy_king',
             email='demo@aa.io',
             password='password',
             state_id=1,
             city_id=2,
             zip_code_id=1,
             sexuality_id=2,
             race_id=1,
             gender_id=4
             ),
         User(username='fruity_honey',
             email='demo@aa.io',
             password='password',
             state_id=1,
             city_id=2,
             zip_code_id=1,
             sexuality_id=2,
             race_id=1,
             gender_id=4
             ),
         User(username='dorothy',
             email='demo@aa.io',
             password='password',
             state_id=1,
             city_id=2,
             zip_code_id=1,
             sexuality_id=2,
             race_id=1,
             gender_id=4
             ),
         User(username='nb_bb',
             email='demo@aa.io',
             password='password',
             state_id=1,
             city_id=2,
             zip_code_id=1,
             sexuality_id=2,
             race_id=1,
             gender_id=4
             ),
         User(username='demo',
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
        State(state="Massachusetts"),
        State(state="Rhode Island"),
        State(state="California"),
        City(city="Seattle"),
        City(city="New York"),
        City(city="Boston"),
        City(city="Providence"),
        City(city="Portland"),
        City(city="San Francisco"),
        City(city="Palo Alto"),
        Zip_Code(zip_code=10005),
        Zip_Code(zip_code=97212)
    ]

    sexualities = [
        "Asexual",
        "Androsexual",
        "Aromantic",
        "Bicurious",
        "Bisexual",
        "Biromantic",
        "Demisexual",
        "Demiromantic",
        "Fluid",
        "Gay",
        "Gynesexual",
        "Heterosexual",
        "Homosexual",
        "Lesbian",
        "LGBTQIA+",
        "Pansexual",
        "Omnisexual",
        "Panromantic",
        "Polysexual",
        "Queer",
        "Straight"
    ]

    genders = [
        "AFAB",
        "Agender",
        "AMAB",
        "Androgyne",
        "Aporagender",
        "Bigender",
        "Cisgender",
        "Demigender",
        "Femme",
        "FTM",
        "GNC",
        "Genderfluid",
        "Genderqueer",
        "Intergender",
        "Intersex",
        "MTF",
        "Non-Binary",
        "Pangender",
        "Polygender",
        "Transfeminine",
        "Transgender",
        "Transmasculine",
        "Two-spirit",
    ]

    races = [
        "White",
        "Asian",
        "African American",
        "Black",
        "Latino",
        "Hispanic",
        "Native American"
    ]

    hc_title = [
        "Doctor",
        "Social Worker",
        "Clinical Coordinator",
        "Consultant",
        "Director of Nursing",
        "Medical Receptionist",
        "Social Services",
        "Audiologist",
        "Anesthesiologist",
        "Be"
        "Ambulatory Nurse",
        "Anesthesiologist",
        "Audiologist",
        "Behavioral Health Charge Nurse",
        "Bereavement Counselor",
        "Cardiac Catheterization Lab Nurse",
        "Cardiovascular Operating Room Nurse",
        "Cardiovascular Technologist",
        "Charge Nurse",
        "Chiropractor",
        "Counselor",
        "Dentist",
        "Dermatology Nurse",
        "Dialysis Nurse",
        "Doctor",
        "Emergency Room Nurse",
        "Endoscopy Nurse",
        "Family Nurse Practitioner",
        "Flight Nurse",
        "Genetic Counselor",
        "Home Health Nurse",
        "Hospice Counselor",
        "Hospice Nurse",
        "House Supervisor Nurse",
        "Intensive Care Nurse",
        "Interventional Radiology Nurse",
        "Labor and Delivery Nurse",
        "Lead Registered Nurse",
        "Legal Nurse Consultant",
        "Licensed Practical Nurse",
        "Licensed Vocational Nurse",
        "Medical Surgery Nurse",
        "Microbiologist",
        "Neonatal Intensive Care Nurse",
        "Nurse",
        "Nurse Anesthetist",
        "Nurse Midwife",
        "Nurse Practitioner",
        "Occupational Health Nurse",
        "Occupational Health and Safety Specialist",
        "Occupational Therapist",
        "Oncology Nurse",
        "Operating Room Nurse",
        "Optician",
        "Optometrist",
        "Orthodontist",
        "Paramedic",
        "Pediatrician",
        "Pediatric Endocrinology Nurse",
        "Pediatric Intensive Care Nurse",
        "Pediatric Nurse",
        "Pediatric Nurse Practitioner",
        "Perioperative Nurse",
        "Pharmacist",
        "Prosthetist",
        "Physician",
        "Podiatrist",
        "Post Anesthesia Nurse",
        "Postpartum Nurse",
        "Progressive Care Nurse",
        "Psychiatric Nurse",
        "Psychiatric Nurse Practitioner",
        "Plastic Surgeon",
        "Public Health Nurse",
        "Registered Nurse",
        "Registered Nurse (RN) Case Manager",
        "Registered Nurse(RN) Data Coordinator",
        "Registered Nurse (RN) First Assistant",
        "Registered Nurse (RN) Geriatric Care",
        "Registered Nurse (RN) Medical Inpatient Services",
        "Registered Nurse (RN) Patient Call Center",
        "Registered Nurse (RN) Student Health Services",
        "Registered Nurse (RN) Telephone Triage",
        "Registered Nurse (RN) Urgent Care",
        "Registered Nurse (RN) Women's Services",
        "Restorative Nurse",
        "Registered Medical Assistant",
        "Respiration (Inhalation) Therapist",
        "School Nurse",
        "Speech-Language Pathologist",
        "Surgeon",
        "Telemetry Nurse",
        "Therapist",
        "Veterinarian",
        "Veterinary Assistant",
        "Veterinary Technologist",
        "Wellness Nurse",
        "Hospice Aide",
        "Massage Therapist",
        "Ocupational Therapist",
        "Nutritionist",

    ]

    hc_provs = [
        Health_Provider(
            first_name="Mandy",
            last_name="Coles",
            state_id=3,
            city_id=3,
            title_id=1,
            ),
        Health_Provider(
            first_name="Erin",
            last_name="Peterson",
            state_id=3,
            city_id=3,
            title_id=2,
            ),
        Health_Provider(
            first_name="Natalia",
            last_name="Bogdanovic",
            state_id=3,
            city_id=3,
            title_id=1,
            ),
        Health_Provider(
            first_name="Andrew",
            last_name="Clark",
            state_id=3,
            city_id=3,
            title_id=1,
            ),
        Health_Provider(
            first_name="Robert",
            last_name="Oats",
            state_id=3,
            city_id=3,
            title_id=1,
            ),
        Health_Provider(
            first_name="Ralph",
            last_name="Vetters",
            state_id=3,
            city_id=3,
            title_id=1,
            ),
        Health_Provider(
            first_name="Pranay",
            last_name="Parikh",
            state_id=3,
            title_id=1,
            ),
        Health_Provider(
            first_name="Michelle",
            last_name="Forcier",
            state_id=4,
            city_id=4,
            title_id=1,
            ),
        Health_Provider(
            first_name="Daniel",
            last_name="Kwan",
            state_id=4,
            city_id=4,
            title_id=1,
            ),
        Health_Provider(
            first_name="Jason",
            last_name="Rafferty",
            state_id=4,
            city_id=4,
            title_id=1,
            ),
        Health_Provider(
            first_name="Jill",
            last_name="Wagner",
            state_id=4,
            city_id=4,
            title_id=2,
            ),
        Health_Provider(
            first_name="Beth",
            last_name="Cronin",
            state_id=4,
            city_id=4,
            title_id=1,
            ),
        Health_Provider(
            last_name="Baker",
            state_id=4,
            city_id=4,
            title_id=1,
            ),
        Health_Provider(
            first_name="Walter",
            last_name="Lin",
            state_id=5,
            city_id=6,
            title_id=1,
            ),
        Health_Provider(
            first_name="Matt",
            last_name="Stevenson",
            state_id=5,
            city_id=7,
            title_id=1,
            ),

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
            "Eating Disorders",
            "Endochronology",
            "Plastic Surgery"
        )
    ]

    services = [
        "Vaginoplasty",
        "Phalloplasty",
        "Scrotoplasty",
        "Metioplasty",
        "Chest surgery",
        "Mastectomy",
        "Facial Feminization",
        "Reduction thyrochondroplasty",
        "Augmentation mammoplasty",
        "Hysterectomy",
        "Oophorectomy",
        "Orchiectomy",
        "Vaginectomy",
        "Facial Hair Removal",
        "Voice Modification",
        "Tucking",
        "Packing",
        "Binding",
        "STD testing",
        "Hormone Replacement Therapy (HRT)",
        "Therapy",
        "Physical Therapy",
        "Mental Health",
        "CBT",
        "Family Therapy",
        "Couples Therapy",
        "Exposure Therapy",
        "Interpersonal Therapy",
        "ABA",
        "Psychotherapy",
        "Trauma work"
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

    for location in locations:
        db.session.add(location)

    for identity in sexualities:
        db.session.add(Sexuality(sexuality=identity))

    for gender in genders:
        db.session.add(Gender(gender=gender))

    for title in hc_title:
         db.session.add(Healthcare_Title(title=title))

    for spec in specialties:
        db.session.add(Specialties(specialty=spec))

    for tag in tags:
        db.session.add(tag)

    for service in services:
        db.session.add(Service(service=service))

    for race in races:
        db.session.add(Race(race=race))

    for user in users:
        db.session.add(user)

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


    db.session.commit()
