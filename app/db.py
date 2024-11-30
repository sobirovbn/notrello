from app.database.core import sync_engine, session_factory, Base
from sqlalchemy import text, insert
from app.database.models import UsersTable, BoardsTable, TasksTable

class DataBase():
  def __init__(self):
    Base.metadata.create_all(sync_engine)

  def dropDatabase(self):
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)

  def isUserExist(self, username: str, password: str) -> bool:
    with session_factory() as session:
      result = session.query(UsersTable).filter(
        UsersTable.username == username,
        UsersTable.password == password
      ).count()
      return result > 0

  def addUser(self, username: str, password: str, email: str):
    with session_factory() as session:
      new_user = UsersTable(
        username=username,
        password=password,
        email=email
      )
      session.add(new_user)
      session.commit()

  def editUserPassword(self, user_id : int, password : str):
    with session_factory() as session:
      result = session.get(UsersTable, user_id)
      result.password = password
      session.commit()

  def changeUserEmail(self, user_id : int, email : str):
    with session_factory() as session:
      result = session.get(UsersTable, user_id)
      result.email = email
      session.commit()

  def getUser(self, username : str, password : str):
    with session_factory() as session:
      result = session.query(UsersTable).filter(
        UsersTable.username == username,
        UsersTable.password == password
      ).first()
      return result.user_id, result.username, result.email

  def deleteUser(self, user_id : int):
    with session_factory() as session:
      user = session.query(UsersTable).filter(UsersTable.user_id == user_id).first()
      if user is not None:
        session.delete(user)
        boards = session.query(BoardsTable).filter(BoardsTable.user_id == user_id).all()
        for board in boards:
          session.delete(board)
        session.commit()

        tasks = session.query(TasksTable).filter(TasksTable.user_id == user_id).all()
        for task in tasks:
          session.delete(task)
        session.commit()

  def isBoardExist(self, user_id: int, board_title: str) -> bool:
    with session_factory() as session:
      result = session.query(BoardsTable).filter(
        BoardsTable.user_id == user_id,
        BoardsTable.title == board_title
      ).count()
      return result > 0

  def addBoard(self, user_id : int, title : str, description : str):
    with session_factory() as session:
      new_board = BoardsTable(
        user_id=user_id,
        title=title,
        description=description
      )
      session.add(new_board)
      session.commit()

  def editBoardTitle(self, board_id : int, title : str):
    with session_factory() as session:
      result = session.get(BoardsTable, board_id)
      result.title = title
      session.commit()

  def editBoardDescription(self, board_id : int, description : str):
    with session_factory() as session:
      result = session.get(BoardsTable, board_id)
      result.description = description
      session.commit()

  def getUserBoards(self, user_id : int):
    with session_factory() as session:
      result = session.query(BoardsTable).filter(
        BoardsTable.user_id == user_id
      ).all()
      res = [board.board_id for board in result]
      return res

  def getBoard(self, board_id : int):
    with session_factory() as session:
      result = session.get(BoardsTable, board_id)
      return result.board_id, result.user_id, result.title, result.description

  def deleteBoard(self, user_id : int, board_id : int):
    with session_factory() as session:
      board = session.query(BoardsTable).filter(BoardsTable.user_id == user_id, BoardsTable.board_id == board_id).first()
      if board is not None:
        session.delete(board)
        session.commit()
        tasks = session.query(TasksTable).filter(TasksTable.board_id == board_id).all()
        for task in tasks:
          session.delete(task)
        session.commit()

  def addTask(self, board_id : int, title : str, description : str, status : str, beginning : str, deadline : str):
    with session_factory() as session:
      new_task = TasksTable(
        board_id=board_id,
        title=title,
        description=description,
        status=status,
        beginning=beginning,
        deadline=deadline
      )
      session.add(new_task)
      session.commit()

  def getTasks(self, board_id : int):
    with session_factory() as session:
      result = session.query(TasksTable).filter(
        TasksTable.board_id == board_id
      ).all()
      res = [task.task_id for task in result]
      return res
  
  def deleteTask(self, board_id : int, task_id : int):
    with session_factory() as session:
      session.delete(session.query(TasksTable).filter_by(board_id=board_id, task_id=task_id).first())
      session.commit()
  
  def editTaskTitle(self, task_id : int, title : str):
    with session_factory() as session:
      result = session.get(TasksTable, task_id)
      result.title = title
      session.commit()

  def editTaskDescription(self, task_id : int, description : str):
    with session_factory() as session:
      result = session.get(TasksTable, task_id)
      result.description = description
      session.commit()

  def editTaskStatus(self, task_id : int, status : str):
    with session_factory() as session:
      result = session.get(TasksTable, task_id)
      result.status = status
      session.commit()
  
  def editTaskBeginning(self, task_id : int, beginning : str):
    with session_factory() as session:
      result = session.get(TasksTable, task_id)
      result.beginning = beginning
      session.commit()
  
  def editTaskDeadline(self, task_id : int, deadline : str):
    with session_factory() as session:
      result = session.get(TasksTable, task_id)
      result.deadline = deadline
      session.commit()

  def getTask(self, task_id : int):
    with session_factory() as session:
      result = session.get(TasksTable, task_id)
      return result.board_id, result.title, result.description, result.status, result.beginning, result.deadline

database = DataBase()
