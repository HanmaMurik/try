from fastapi import FastAPI
import uvicorn
from database import Base, engine

from student_marks import marks_router
from profile import profile_router
from registration import student_router
from comments import comment_router

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

uvicorn.run(app, host='0.0.0.0')

app.include_router(student_router)
app.include_router(profile_router)
app.include_router(marks_router)
app.include_router(comment_router)

