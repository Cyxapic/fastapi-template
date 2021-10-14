from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseSettings


class Settings(BaseSettings):
    db_name: str
    db_user: str
    db_password: str
    db_host: str = 'localhost'
    db_port: int = 5432

    class Config:
        env_file = ".env"

    @property
    def database_url(self):
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:5432/{self.db_name}"


settings = Settings()

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    Base.metadata.create_all(bind=engine)
