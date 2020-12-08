from backend.models.user import (User, Gender, Race, Sexuality,
                            Healthcare_Title, State, City, Zip_Code, Health_Provider,
                             Tag, Review, Review_Tag, Specialty, Service)
from backend import app, db
from dotenv import load_dotenv

load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()

    states = [
        "New York",
        "Oregon",
        "Massachusetts",
        "Rhode Island",
        "California",
    ]

    cities = [
        "Seattle",
        "New York",
        "Boston",
        "Providence",
        "Portland",
        "San Francisco",
        "Palo Alto",
    ]

    zip_codes = [
        10005,
        97212
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

    specialties = [
        "Eating disorders",
        "Nutrition",
        "Endocrinology",
        "Plastic surgery",
        "Dermatology",
        "Otolaryngology",
        "Cognitive Behavioral Therapy",
        "Phlebotomy",
        "Gastroenterology",
        "Cardiology",
        "Primary Care",
        "Physical Therapy",
        "Radiology",
        "Pediatrics",
        "Ophthalmology",
        "Optometry",
        "Neurosurgery",
        "Neurology",
        "Talk therapy",
        "Orthopedics",
        "Obstetrics and Gynecology",
        "Psychiatry",
        "Oncology",
        "Anesthesiology",
        "Orthodontics",
        "Dentistry",
        "Urology",
        "General Surgery",
        "Vascular surgery",
        "Nephrology",
        "Pulmonology",
        "Geriatrics",
        "Rheumatology",
        "Sports Medicine",
        "Hematology",
        "Infectious Disease",
        "Occupational Therapy",
        "Addiction psychology",
        "Allergy and immunology",
        "Adolescent medicine",
        "Gender care",
        "Child and adolescent psychology",
        "Craneofacial surgery",
        "Emergency Medicine",
        "Dialectical behavior therapy",
        "Trauma therapy",
        "Family planning",
        "Hospice",
        "Internal medicine",
        "Toxicology",
        "Osteopathic medicine",
        "Neonatal-perinatal medicine",
        "Preventative medicine",
        "Pulmonary disease",
        "Thoracic surgery",
        "Medical genetics",
        "Light therapy",
        "Aversion therapy",
        "Applied behavior analysis",
        "Individual therapy",
        "Group therapy",
        "Family therapy",
        "Art therapy",
        "Bibliotherapy",
        "Biofeedback",
        "Exposure and response prevention",
        "Marriage counseling",
        "Motivational interviewing",
        "Music therapy",
        "Neurofeedback",
        "Play therapy",
        "Person centered therapy",
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


    hc_titles = [
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
            first_name='',
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

    users = [
        User(username='demo',
             email='demo@aa.io',
             password='password',
             state_id=1,
             city_id=2,
             zip_code_id=1,
             race_id=1,
             ),
         User(username='mrlockin',
             email='mrlockin@aa.io',
             password='password',
             state_id=1,
             city_id=2,
             zip_code_id=1,
             race_id=1,
             ),
         User(username='pansy_king',
             email='pansy_king@aa.io',
             password='password',
             state_id=1,
             city_id=2,
             zip_code_id=1,
             race_id=1,
             ),
         User(username='fruity_honey',
             email='fruity_honey@aa.io',
             password='password',
             state_id=1,
             city_id=2,
             zip_code_id=1,
             race_id=1,
             ),
         User(username='dorothy',
             email='dorothy@aa.io',
             password='password',
             state_id=1,
             city_id=2,
             zip_code_id=1,
             race_id=1,
             ),
         User(username='nb_bb',
             email='nb_bb@aa.io',
             password='password',
             state_id=1,
             city_id=2,
             zip_code_id=1,
             race_id=1,
             ),
         User(username='blukitten',
             email='blukitten@aa.io',
             password='password',
             state_id=1,
             city_id=2,
             zip_code_id=1,
             race_id=1
             )
    ]

    tags = [
        "Compassionate",
        "Timely",
        "Considerate",
        "Inclusive",
        "Competent",
        "Trans",
        "Knowledgable",
        "Extra time",
        "Bedside Manner"
        "Racist",
        "Misgendered",
        "Transphobic",
        "Fatphobic",
        "Homophobic",
        "Ableist",
        "Correct pronouns",
        "Non-monogamy",
    ]

    reviews = [
        Review(
            health_provider_id=1,
            good="Compassionate and great bedside manner",
            bad="kind of awkward",
            user_id=1,
            rating=8
        ),
        Review(
            health_provider_id=1,
            good='Mandy does amazing work for and with trans youth. I have taken all of the kids from the group home I work for to see her when possible. She is competent and always available for emergency help. Could not love her more.',
            bad='Nothing, she is perfect.',
            user_id=2,
            rating=10
        ),
        Review(
            health_provider_id=2,
            good="She is wonderful. She works with adolecents at BMC's CATCH program",
            bad='BMC is super busy.',
            user_id=3,
            rating=7
        ),
        Review(
            health_provider_id=2,
            good="incredibly thorough, gives teenagers agency in their own care and ensures access to expansive services outside of just medical care.",
            bad='BMC is in the middle of an area with intravenous drug use which has made some of the youth I bring there uncomfortable.',
            user_id=4,
            rating=9
        ),
        Review(
            health_provider_id=2,
            good="Her understanding of gender is highly trans competent",
            bad='Bathrooms are dirty and the ones that are accessible are strictly gendered.',
            user_id=5,
            rating=8
        ),
        Review(
            health_provider_id=3,
            good="She has an advanced understanding of gender and she advocated fiercly for youth.",
            bad='She reads as kind of cold and can be blunt.',
            user_id=5,
            rating=8
        ),
        Review(
            health_provider_id=3,
            good="She is wonderful but some people don't like interacting with her because she can be kind of scary. She makes sure her clients have a voice in their care and medication.",
            bad='Nothing bad.',
            user_id=6,
            rating=9
        ),
        Review(
            health_provider_id=4,
            good="He's fine, the only interactions I've had with him were with a tricky kid who wanted to be on aderall. He responded pretty well to her being aggressive.",
            bad='He definitely has some learning to do around gender',
            user_id=7,
            rating=6
        ),
        Review(
            health_provider_id=5,
            good="I haven't been to him directly but I have not heard good things.",
            bad='Transphobic',
            user_id=1,
            rating=1
        ),
        Review(
            health_provider_id=6,
            good="Overall he is fine.",
            bad="Dr Vetters has been working in the field for a long time and is clearly burnt out. He doesn't give the kind of special care that one would hope for out of a doctor",
            user_id=2,
            rating=6
        ),
        Review(
            health_provider_id=7,
            good="He was my plastic surgeon for top surgery and he gave so many options and made sure my chest would look exactly how I wanted it to. I LOVED him.",
            bad="His office isn't very well resourced.",
            user_id=3,
            rating=10
        ),
        Review(
            health_provider_id=8,
            good="I've heard good things about her being the best Hormone Replacement person in Rhode Island.",
            bad="Haven't actually been to her but heard no bad things.",
            user_id=4,
            rating=9
        ),
        Review(
            health_provider_id=9,
            good="He did a good job on my top surgery.",
            bad="He is not trans competent at all. He misgendered me and during our pre-op appointments said a number of comments that triggered my dysphoria.",
            user_id=5,
            rating=1
        ),
        Review(
            health_provider_id=9,
            good="idk",
            bad="He was my partner's surgeon for a double mastectomy. They were misgendered every step of the way from the nurses to the front desk people to the anesthesiologist, even when I had gone ahead to make sure everyone knew their pronouns. He does the most top surgeries in Rhode Island I'm pretty sure and he misgendered my partner throughout! I cannot. It was horrible but the surgery went fine.",
            user_id=5,
            rating=1
        )
    ]

    review_tags = [
        Review_Tag(
            quality=True,
            review_id=1,
            tag_id=1
        ),
        Review_Tag(
            quality=True,
            review_id=1,
            tag_id=8
        ),
        Review_Tag(
            quality=True,
            review_id=2,
            tag_id=6
        ),
        Review_Tag(
            quality=True,
            review_id=3,
            tag_id=5
        ),
        Review_Tag(
            quality=False,
            review_id=3,
            tag_id=6
        ),
    ]

    for state in states:
        db.session.add(State(state=state))

    for city in cities:
        db.session.add(City(city=city))

    for zc in zip_codes:
        db.session.add(Zip_Code(zip_code=zc))

    for gender in genders:
        db.session.add(Gender(gender=gender))

    for race in races:
        db.session.add(Race(race=race))

    for sexuality in sexualities:
        db.session.add(Sexuality(sexuality=sexuality))

    for specialty in specialties:
        db.session.add(Specialty(specialty=specialty))

    for service in services:
        db.session.add(Service(service=service))

    for title in hc_titles:
        db.session.add(Healthcare_Title(title=title))

    for hc_prov in hc_provs:
        db.session.add(hc_prov)

    for user in users:
        db.session.add(user)

    for tag in tags:
        db.session.add(Tag(word=tag))

    for review in reviews:
        db.session.add(review)

    for tag in review_tags:
        db.session.add(tag)

    db.session.commit()
