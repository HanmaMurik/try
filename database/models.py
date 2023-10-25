from sqlalchemy import Integer, DateTime, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)



class StudentsMark(Base):
    __tablename__ = 'students_mark'
    mark_id = Column(Integer, autoincrement=True, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    mark_text = Column(String)



class MarksComment(Base):
    __tablename__ = 'mark_comments'
    comment_id = Column(Integer, autoincrement=True, primary_key=True)

    mark_id = Column(Integer, ForeignKey('mark_comments.mark_id'))
    student_id = Column(Integer, ForeignKey('students.student_id'))

    comment_text = Column(String)
    publish_date = Column(DateTime)

    student_fk = relationship(Student, lazy='subquery')
    mark_fk = relationship(StudentsMark, lazy='subquery')



