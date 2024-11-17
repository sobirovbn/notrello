from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  DB_PATH: str
  DB_NAME: str

  @property
  def db_url(self):
      return f"sqlite:///{self.DB_PATH}{self.DB_NAME}"
  
  model_config = SettingsConfigDict(env_file=".env")

setting = Settings()
sync_engine = create_engine(
  url=setting.db_url
)

session_factory = sessionmaker(sync_engine)

class Base(DeclarativeBase):
  pass
