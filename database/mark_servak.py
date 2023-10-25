from database.models import StudentsMark
from database import get_db


def get_all_marks():
    db = next(get_db())

    all_marks = db.query(StudentsMark).all()

    return all_marks


def get_exact_mark(mark_id):
    db = next(get_db())

    exact_mark = db.query(StudentsMark).filter_by(mark_id=mark_id).first()

    if exact_mark:
        return exact_mark

    return "Mark was not defined"


def add_new_mark(student_id, mark_text, publish_date):
    db = next(get_db())

    new_mark = StudentsMark(student_id=student_id, mark_text=mark_text, publish_date=publish_date)

    db.add(new_mark)
    db.commit()

    return new_mark.post_id


def edit_mark_text(mark_id, new_text):
    db = next(get_db())

    exact_mark = db.query(StudentsMark).filter_by(mark_id=mark_id).first()

    if exact_mark:
        exact_mark.mark_text = new_text
        db.commit()

        return "Comment was successfully changed"

    return "Mark was not defined"


def delete_mark(mark_id):
    db = next(get_db())

    exact_mark = db.query(StudentsMark).filter_by(mark_id=mark_id).first()

    if exact_mark:
        db.delete(exact_mark)
        db.commit()

        return "Mark was deleted"

    return "Mark was not defined"





