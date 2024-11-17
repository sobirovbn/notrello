"""
Create
Read
Update
Delete
"""

from app.task.schemas import *
from app.db import database

def getTask(taskid: int) -> Task:
    board_id, title, description, status = database.getTask(taskid)
    return {
        "status": "success",
        "taskid": taskid,
        "boardid": board_id,
        "title": title,
        "description": description,
        "task_status": status
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
