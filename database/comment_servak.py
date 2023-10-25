from database.models import MarksComment
from database import get_db


def get_exact_mark_comment(mark_id):
    db = next(get_db())

    exact_mark_comment = db.query(MarksComment).filter_by(mark_id=mark_id).all()

    return exact_mark_comment


def add_new_comment(mark_id, student_id, comment_text, publish_date):
    db = next(get_db())

    new_comment = MarksComment(mark_id=mark_id, student_id=student_id, comment_text=comment_text, publish_date=publish_date)

    db.add(new_comment)
    db.commit()

    return 'Comment was successfully added'


def change_exact_comment(comment_id, new_comment_text):
    db = next(get_db())

    exact_comment = db.query(MarksComment).filter_by(comment_id=comment_id).first()

    if exact_comment:
        exact_comment.comment_text = new_comment_text
        db.commit()

        return "Successfully changed"

    return "Comment was not defined"


def delete_exact_comment(comment_id):
    db = next(get_db())

    exact_comment = db.query(MarksComment).filter_by(comment_id=comment_id).first()

    if exact_comment:
        db.delete(exact_comment)
        db.commit()

        return "Comment was successfully deleted"

    return "Comment was not defined"
