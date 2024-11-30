from fastapi import APIRouter
from app.task import crud
from app.task.schemas import *

router = APIRouter(
    prefix="/api/task",
    tags=["Task"],
)

@router.post("/get")
def get_task(form: TaskForm) -> Task:
    return crud.getTask(form.taskid)

@router.put("/change/title")
def change_title(form: ChangeTitleForm) -> Status:
    return crud.changeTitle(form.taskid, form.new_title)

@router.put("/change/desc")
def change_description(form: ChangeDescForm) -> Status:
    return crud.changeDesc(form.taskid, form.new_description)

@router.put("/change/status")
def change_status(form: ChangeStatusForm) -> Status:
    return crud.changeStatus(form.taskid, form.new_status)

@router.put("/change/beginning")
def change_status(form: ChangeBeginningForm) -> Status:
    return crud.changeBeginning(form.taskid, form.new_beginning)

@router.put("/change/deadline")
def change_status(form: ChangeDeadlineForm) -> Status:
    return crud.changeDeadline(form.taskid, form.new_deadline)