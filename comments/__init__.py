from fastapi import APIRouter


comment_router = APIRouter(prefix='/comments', tags=['Comments to marks'])

from comments import comments_api
