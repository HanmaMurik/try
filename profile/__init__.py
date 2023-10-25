from fastapi import APIRouter


profile_router = APIRouter(prefix='/profile', tags=['Profile of student'])


from profile import profile_api
