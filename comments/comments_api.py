from fastapi import Body
from datetime import datetime

from comments import comment_router
from database.comment_servak import get_exact_mark_comment, add_new_comment, delete_exact_comment, change_exact_comment


@comment_router.get('/mark-comments')
async def get_mark_comments(student_id: int):

    result = get_exact_mark_comment(student_id)

    return {'status': 1, 'message': result}


@comment_router.post('/add-comment')
async def add_new_comment(student_id: int = Body(...), mark_id: int = Body(...), comment_text: str = Body(...)):

    result = add_new_comment(mark_id=mark_id, student_id=student_id, comment_text=comment_text, publish_date=datetime.now())

    return {'status': 1, 'message': result}


@comment_router.put('/edit-comment')
async def edit_exact_comment(comment_id: int = Body(...), new_comment_text: str = Body(...)):

    result = change_exact_comment(comment_id, new_comment_text)

    return {'status': 1, 'message': result}


@comment_router.delete('/delete-comment')
async def delete_exact_comment(comment_id: int):
    result = delete_exact_comment(comment_id)

    return {'status': 1, 'message': result}



