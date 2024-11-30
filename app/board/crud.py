"""
Create
Read
Update
Delete
"""
from app.board.schemas import *
from app.db import database
from fn import *

def getBoard(boardid: int) -> Board:
    boardid, userid, title, description = database.getBoard(boardid)
    return {
        "status": "success",
        "boardid": boardid,
        "userid": userid,
        "title": title,
        "description": description
    }

def getTasks(boardid: int) -> List:
    tasks = database.getTasks(boardid)
    return {
        "status": "success",
        "ids": tasks
    }

def changeTitle(boardid: int, new_title: str) -> Status:
    database.editBoardTitle(boardid, new_title)
    return success

def changeDesc(boardid: int, new_desc: str) -> Status:
    database.editBoardDescription(boardid, new_desc)
    return success

def addTask(boardid: int, title: str, desc: str, status: str, beginning: str, deadline: str) -> Status:
    if not (checkTime(beginning) and checkTime(deadline)):
        return failed
    database.addTask(boardid, title, desc, status, beginning, deadline)
    return success

def deleteTask(boardid: int, taskid: int) -> Status:
    database.deleteTask(boardid, taskid)
    return success
