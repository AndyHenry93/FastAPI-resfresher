from typing import Optional

from pydantic import BaseModel


class Base(BaseModel):
    pass


class Task(Base):
    title: str
    description: str
    status: str


class TaskV2(Base):
    title: str
    description: str
    status: str
    priority: Optional[str] = None


class TaskResponse(Task):
    id: int


class TaskV2Response(TaskV2):
    id: int
