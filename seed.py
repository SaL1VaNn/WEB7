from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Subject, Grade
import random

fake = Faker()
# З'єднання з базою даних
engine = create_engine('postgresql://SaL1VaNn:hetshot53@localhost:5432/Sali')
# Створення таблиць
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

for _ in range(30):
    student = Student(name=fake.name())
    session.add(student)

group_names = ["Group A", "Group B", "Group C"]
for group_name in group_names:
    group = Group(name=group_name)
    session.add(group)

for _ in range(5):
    teacher = Teacher(name=fake.name())
    session.add(teacher)

subjects = ["Math", "Science", "History", "English", "Computer Science"]
for subject_name in subjects:
    teacher = random.choice(session.query(Teacher).all())
    subject = Subject(name=subject_name, teacher=teacher)
    session.add(subject)

students = session.query(Student).all()
subjects = session.query(Subject).all()
for student in students:
    for subject in subjects:
        score = random.uniform(2.0, 5.0)
        grade = Grade(student=student, subject=subject, score=score)
        session.add(grade)

# Збереження змін до бази даних
session.commit()
