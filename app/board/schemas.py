from pydantic import BaseModel
from app.user.schemas import Status, List, failed, success

class Board(Status):
    boardid: int
    userid: int
    title: str
    description: str

class BoardForm(BaseModel):
    boardid: int

class ChangeTitleForm(BoardForm):
    new_title: str

class ChangeDescForm(BoardForm):
    new_description: str

class AddTaskForm(BoardForm):
    title: str
    description: str
    status: str

class DeleteTaskForm(BoardForm):
    taskid: int
