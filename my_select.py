from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Student, Grade, Subject

engine = create_engine('postgresql://SaL1VaNn:hetshot53@localhost:5432/Sali')
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів
    students = (
        session.query(Student)
        .join(Grade)
        .group_by(Student.id)
        .order_by(func.avg(Grade.score).desc())
        .limit(5)
        .all()
    )
    return students

def select_2(subject_name):
    # Знайти студента із найвищим середнім балом з певного предмета
    subject = session.query(Subject).filter_by(name=subject_name).first()
    if subject:
        student = (
            session.query(Student)
            .join(Grade)
            .filter(Grade.subject_id == subject.id)
            .group_by(Student.id)
            .order_by(func.avg(Grade.score).desc())
            .first()
        )
        return student
    else:
        return None



if __name__ == "__main__":
    result_1 = select_1()
    print("5 студентів із найбільшим середнім балом:")
    for student in result_1:
        print(f"{student.name}")

    result_2 = select_2("Math")
    if result_2:
        print(f"Студент із найвищим середнім балом з математики: {result_2.name}")
    else:
        print("Предмет не знайдено")
