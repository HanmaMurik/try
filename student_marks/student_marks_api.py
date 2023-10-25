from fastapi import Body
from datetime import datetime

from student_marks import marks_router
from database.mark_servak import add_new_mark, delete_mark, edit_mark_text, get_exact_mark, get_all_marks


@marks_router.post('/new-post')
async def new_mark(student_id: int = Body(...), mark_text: str = Body(...)):

    result = add_new_mark(student_id=student_id, mark_text=mark_text, publish_date=datetime.now())

    return {'status': 1, 'message': result}


@marks_router.get('/all-posts')
async def get_all_marks():
    result = get_all_marks()

    return {'status': 1, 'message': result}


@marks_router.get('/exact-post')
async def get_exact_mark(mark_id: int):
    result = get_exact_mark(mark_id)

    return {'status': 1, 'message': result}


@marks_router.delete('/delete-post')
async def delete_mark(mark_id: int):
    result = delete_mark(mark_id)

    return {'status': 1, 'message': result}


@marks_router.put('/edit-post')
async def change_mark(mark_id: int = Body(...), new_text: str = Body(...)):

    result = edit_mark_text(mark_id, new_text)

    return {'status': 1, 'message': result}

