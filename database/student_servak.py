from database.models import Student
from database import get_db

def get_all_students():
    db = next(get_db())

    all_students = db.query(Student).all()

    return all_students

def get_exact_student(student_id):
    db = next(get_db())

    exact_student = db.query(Student).filter_by(student_id=student_id).first()

    if exact_student:
        return exact_student

    return False


def add_new_student(name, surname, email, password):
    db = next(get_db())

    checker = db.query(Student).filter_by(email=email).first()

    if checker:
        return "This email is already exist"

    else:
        new_student = Student(name=name, surname=surname, email=email, password=password)

        db.add(new_student)
        db.commit()

        return "Student was successfully added"


def login_student(email, password):
    db = next(get_db())

    student = db.query(Student).filter_by(email=email, password=password).first()

    if student:
        return student

    return "Error_macros"


def edit_student_info(student_id, edit_info, new_info):
    db = next(get_db())

    exact_student = get_exact_student(student_id)

    if exact_student:
        if  edit_info == 'email':
            exact_student.email = new_info

        elif edit_info == 'password':
            exact_student.password = new_info

        elif edit_info == 'name':
            exact_student.name = new_info

        db.commit()

        return "Information was successfully changed"

    return "Student was not defined"


def delete_student(student_id):
    db = next(get_db())

    student = db.query(Student).filter_by(student_id=student_id).first()

    if student:
        db.delete(student)
        db.commit()

        return "Student was successfully deleted"

    return "Student was not defined"


