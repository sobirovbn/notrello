from sqlalchemy.orm import Mapped, mapped_column
from app.database.core import Base

class UsersTable(Base):
  __tablename__ = "users"
  user_id: Mapped[int] = mapped_column(primary_key=True)
  username: Mapped[str]
  password: Mapped[str]
  email: Mapped[str]

class BoardsTable(Base):
  __tablename__ = "boards"
  board_id: Mapped[int] = mapped_column(primary_key=True)
  user_id: Mapped[int]
  title: Mapped[str]
  description: Mapped[str]

class TasksTable(Base):
  __tablename__ = "tasks"
  task_id: Mapped[int] = mapped_column(primary_key=True)
  board_id: Mapped[int]
  title: Mapped[str]
  description: Mapped[str]
  status: Mapped[str]
