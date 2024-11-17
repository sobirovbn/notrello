"""
Create
Read
Update
Delete
"""
from app.user.schemas import *
from app.db import database

def createUser(username: str, password: str, email: str) -> Status:   
    if database.isUserExist(username, password):
        return failed
    database.addUser(username, password, email)
    return success

def getUser(username: str, password: str) -> User:
    if not database.isUserExist(username, password):
        return {
            "status": "fail",
            "userid": -1,
            "username": "lol",
            "email": "lol",
        }
    userid, username, email = database.getUser(username, password)
    return {
        "status": "success",
        "userid": userid,
        "username": username,
        "email": email
    }

def getBoards(userid: int) -> List:
    return {
        "status": "success",
        "ids": database.getUserBoards(userid)
    }

def changePassword(userid: int, new_password: str) -> Status:
    database.editUserPassword(userid, new_password)
    return success

def changeEmail(userid: int, new_email: str) -> Status:
    database.changeUserEmail(userid, new_email)
    return success

def addBoard(userid: int, title: str, desc: str) -> Status: 
    database.addBoard(userid, title, desc)
    return success

def deleteBoard(userid: int, boardid: int) -> Status:
    database.deleteBoard(userid, boardid)
    return success

def deleteUser(userid: int) -> Status:
    database.deleteUser(userid)
    return success
