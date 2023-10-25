from fastapi import APIRouter


marks_router = APIRouter(prefix='/mark', tags=['Student marks'])

from student_marks import student_marks_api


