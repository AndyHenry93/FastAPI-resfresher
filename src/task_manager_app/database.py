from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test_task_v2.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    title: Mapped[str]
    description: Mapped[str]
    status: Mapped[str]
    priority: Mapped[Optional[str]] = mapped_column(
        nullable=True,
    )


Base.metadata.create_all(bind=engine)
