from fastapi import Body

from profile import profile_router
from database.student_servak import get_exact_student, get_all_students, edit_student_info


@profile_router.get('/exact-student')
async def exact_student_info(student_id: int):
    result = get_exact_student(student_id)

    if result:
        return {'status': 1, 'message': result}

    else:
        return {'status': 0, 'message': 'Student was not defined'}


@profile_router.get('/all-students')
async def all_students_info():
    result = get_all_students()

    return {'status': 1, 'message': result}


@profile_router.put('/edit-students')
async def edit_student(student_id: int = Body(...), new_info: str = Body(...), edit_info: str = Body(...)):

    result = edit_student_info(student_id=student_id, edit_info=edit_info, new_info=new_info)

    return {'status': 1, 'message': result}
