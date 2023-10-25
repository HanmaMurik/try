from fastapi import APIRouter
from pydantic import BaseModel

student_router = APIRouter(prefix='/student', tags=['Student'])


class RegisterModel(BaseModel):
    name: str
    surname: str
    email: str
    password: str

class LoginModel(BaseModel):
    email: str
    password: str


from registration import registration_api
