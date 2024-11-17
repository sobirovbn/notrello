from pydantic import BaseModel

class Status(BaseModel):
    status: str

class List(Status):
    ids: list[int]

class RegForm(BaseModel):
    username: str
    password: str
    email: str

class LoginForm(BaseModel):
    username: str
    password: str

class User(Status):
    userid: int
    username: str
    email: str

class UserForm(BaseModel):
    userid: int

class ChangePswForm(UserForm):
    new_password: str

class ChangeEmailForm(UserForm):
    new_email: str

class AddBoardForm(UserForm):
    userid: int
    title: str
    description: str

class DeleteBoardForm(UserForm):
    boardid: int

failed = {
    "status": "failed"
}

success = {
    "status": "success"
}
