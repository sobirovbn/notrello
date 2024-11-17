from fastapi import APIRouter
from app.user import crud
from app.user.schemas import *

router = APIRouter(
    prefix="/api/user",
    tags=["User"],
)

@router.post("/create")
def create_user(form: RegForm) -> Status:
    return crud.createUser(form.username, form.password, form.email)

@router.post("/get")
def get_user(form: LoginForm) -> User:
    return crud.getUser(form.username, form.password)

@router.post("/get/boards")
def get_boards(form: UserForm) -> List:
    return crud.getBoards(form.userid)

@router.put("/change/password")
def change_password(form: ChangePswForm) -> Status:
    return crud.changePassword(form.userid, form.new_password)

@router.put("/change/email")
def change_email(form: ChangeEmailForm) -> Status:
    return crud.changeEmail(form.userid, form.new_email)

@router.put("/add/board")
def add_board(form: AddBoardForm) -> Status:
    return crud.addBoard(form.userid, form.title, form.description)

@router.delete("/delete/board")
def delete_board(form: DeleteBoardForm) -> Status:
    return crud.deleteBoard(form.userid, form.boardid)

@router.delete("/delete")
def delete_user(form: UserForm) -> Status:
    return crud.deleteUser(form.userid)
