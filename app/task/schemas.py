from pydantic import BaseModel
from app.user.schemas import Status, success, failed
from app.board.schemas import BoardForm

class TaskForm(BoardForm):
    taskid: int

class ChangeTitleForm(TaskForm):
    new_title: str

class ChangeDescForm(TaskForm):
    new_description: str

class ChangeStatusForm(TaskForm):
    new_status: str

class Task(Status):
    taskid: int
    boardid: int
    title: str
    description: str
    task_status: str
