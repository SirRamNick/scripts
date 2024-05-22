import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random

cred = credentials.Certificate('scripts/oats-cred.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

alumni_count = 1501


def generate_alumni_data():
    doc = db.collection('alumni')
    degrees = ['BSCS', 'ACT', 'BEEd-GE', 'BSEd-English', 'BSEd-Math', 'AB English', 'BSBA-MM', 'BSBA-HRM', 'BS Entrep', 'BSHM/BSHRM', 'BSTM ', 'TCP']
    first_names = ['Rammne', 'Ira', 'Rovic', 'Angie', 'AC', 'Christina', 'Christian', 'Xavier', 'Nicholas', 'Kristianne', 'Amparito', 'Maria', 'Kent']
    last_names = ['Tiongson', 'Aliman', 'Richards', 'Pre', 'Banez', 'Ortricio', 'Salvador', 'Gadiano', 'Rivera', 'Garcia', 'Dela Cruz']
    employment_status = ['Privately Employed', 'Government Employed', 'Self-Employed', 'Others']
    occupation = ['pro player', 'programmer', 'software developer', 'educator', 'business owner', 'data analyst', 'teacher', 'bartender', 'housewife', 'freelance']
    date_of_birth = ['May 3, 1998', 'May 5, 1998', 'June 21, 1970', 'December 12, 1986', 'September 16, 2000']
    question_1 = ['Answer to this question (dummy data)', 'Dummy Answer for this question (Open Ended)', 'Open Ended question answer']
    question_2 = ['Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree']
    question_3 = ['Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree']
    question_4 = ['A', 'B', 'C', 'D', 'E']
    question_5 = ['Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree']
    question_6 = ['Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree']
    sex = ['Female', 'Male']
    for _ in range(alumni_count):
        doc.add(
            {
                'first_name': first_names[random.randint(0, len(first_names) - 1)],
                'last_name': last_names[random.randint(0, len(last_names) - 1)],
                'middle_name': last_names[random.randint(0, len(last_names) - 1)],
                'employment_status': employment_status[random.randint(0, len(employment_status) - 1)],
                'occupation': occupation[random.randint(0, len(occupation) - 1)],
                'email': f'{first_names[random.randint(0, len(first_names) - 1)]}.{last_names[random.randint(0, len(last_names) - 1)]}@email.com',
                'date_of_birth': date_of_birth[random.randint(0, len(date_of_birth) - 1)],
                'degree': degrees[random.randint(0, len(degrees) - 1)],
                'year_graduated': random.randint(2002, 2023),
                'question_1': question_1[random.randint(0, len(question_1) - 1)],
                'question_2': question_2[random.randint(0, len(question_2) - 1)],
                'question_3': question_3[random.randint(0, len(question_3) - 1)],
                'question_4': question_4[random.randint(0, len(question_4) - 1)],
                'question_5': question_5[random.randint(0, len(question_5) - 1)],
                'question_6': question_6[random.randint(0, len(question_6) - 1)],
            }
        )

def generate_employment_status_data():
    for year in range(2002, 2024):
        doc = db.collection('employment_status').document(str(year))
        doc.set({'privately_employed': random.randint(0, alumni_count - 1),
                 'government_employed': random.randint(0, alumni_count - 1),
                 'self_employed': random.randint(0, alumni_count - 1),
                 'others': random.randint(0, 100)},
                merge=True)
        
def generate_alumni_by_year():
    for year in range(2002, 2024):
        doc = db.collection('alumni_by_year').document(str(year))
        doc.set({'value': random.randint(20, 201), 'year': year},merge=True)

def generate_question_data():
    degrees = ['BSCS', 'ACT', 'BEEd-GE', 'BSEd-English', 'BSEd-Math', 'AB English', 'BSBA-MM', 'BSBA-HRM', 'BS Entrep', 'BSHM(BSHRM)', 'BSTM ', 'TCP']
    
    for degree in degrees:
        doc = db.collection('question_2').document(str(degree))
        doc.set({'degree': degree,
                 'strongly_agree': random.randint(0,alumni_count - 1),
                 'agree': random.randint(0,alumni_count - 1),
                 'neutral': random.randint(0,alumni_count - 1),
                 'disagree': random.randint(0,alumni_count - 1),
                 'strongly_disagree': random.randint(0,alumni_count - 1)}, merge=True)
        
    for degree in degrees:
        doc = db.collection('question_3').document(str(degree))
        doc.set({'degree': degree,
                 'strongly_agree': random.randint(0,alumni_count - 1),
                 'agree': random.randint(0,alumni_count - 1),
                 'neutral': random.randint(0,alumni_count - 1),
                 'disagree': random.randint(0,alumni_count - 1),
                 'strongly_disagree': random.randint(0,alumni_count - 1)}, merge=True)
        
    for degree in degrees:
        doc = db.collection('question_5').document(str(degree))
        doc.set({'degree': degree,
                 'strongly_agree': random.randint(0,alumni_count - 1),
                 'agree': random.randint(0,alumni_count - 1),
                 'neutral': random.randint(0,alumni_count - 1),
                 'disagree': random.randint(0,alumni_count - 1),
                 'strongly_disagree': random.randint(0,alumni_count - 1)}, merge=True)
        
    for degree in degrees:
        doc = db.collection('question_6').document(str(degree))
        doc.set({'degree': degree,
                 'strongly_agree': random.randint(0,alumni_count - 1),
                 'agree': random.randint(0,alumni_count - 1),
                 'neutral': random.randint(0,alumni_count - 1),
                 'disagree': random.randint(0,alumni_count - 1),
                 'strongly_disagree': random.randint(0,alumni_count - 1)}, merge=True)
    

generate_alumni_data()
generate_employment_status_data()
generate_alumni_by_year()
generate_question_data()
