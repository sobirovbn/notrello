"""
Create
Read
Update
Delete
"""

from app.task.schemas import *
from app.db import database
from fn import *

def getTask(taskid: int) -> Task:
    board_id, title, description, status, beginning, deadline = database.getTask(taskid)
    return {
        "status": "success",
        "taskid": taskid,
        "boardid": board_id,
        "title": title,
        "description": description,
        "task_status": status,
        "beginning": beginning,
        "deadline": deadline
    }

def changeTitle(taskid: int, new_title: str) -> Status:
    database.editTaskTitle(taskid, new_title)
    return success

def changeDesc(taskid: int, new_desc: str) -> Status:
    database.editTaskDescription(taskid, new_desc)
    return success

def changeStatus(taskid: int, status: str) -> Status:
    database.editTaskStatus(taskid, status)
    return success

def changeBeginning(taskid: int, beginning: str) -> Status:
    if not checkTime(beginning):
        return failed
    database.editTaskBeginning(taskid, beginning)
    return success

def changeDeadline(taskid: int, deadline: str) -> Status:
    if not checkTime(deadline):
        return failed
    database.editTaskDeadline(taskid, deadline)
    return success