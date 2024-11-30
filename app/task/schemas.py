from pydantic import BaseModel
from app.user.schemas import Status, success, failed

class TaskForm(BaseModel):
    taskid: int

class ChangeTitleForm(TaskForm):
    new_title: str

class ChangeDescForm(TaskForm):
    new_description: str

class ChangeStatusForm(TaskForm):
    new_status: str

class ChangeBeginningForm(TaskForm):
    new_beginning: str

class ChangeDeadlineForm(TaskForm):
    new_deadline: str

class Task(Status):
    taskid: int
    boardid: int
    title: str
    description: str
    task_status: str
    beginning: str
    deadline: str