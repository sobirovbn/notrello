from fastapi import APIRouter
from app.board import crud
from app.board.schemas import *

router = APIRouter(
    tags=["Board"],
    prefix="/api/board"
)

@router.post("/get")
def get_board(form: BoardForm) -> Board:
    return crud.getBoard(form.boardid)

@router.post("/get/tasks")
def get_tasks(form: BoardForm) -> List:
    return crud.getTasks(form.boardid)

@router.post("/add/task")
def add_task(form: AddTaskForm) -> Status:
    return crud.addTask(form.boardid, form.title, form.description, form.status)

@router.put("/change/title")
def change_title(form: ChangeTitleForm) -> Status:
    return crud.changeTitle(form.boardid, form.new_title)

@router.put("/change/desc")
def change_description(form: ChangeDescForm) -> Status:
    return crud.changeDesc(form.boardid, form.new_description)

@router.delete("/delete/task")
def delete_task(form: DeleteTaskForm) -> Status:
    return crud.deleteTask(form.boardid, form.taskid)
