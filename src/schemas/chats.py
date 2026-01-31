from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

from src.schemas.messages import MessageOut


class ChatCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)


class ChatOut(BaseModel):
    id: int
    title: str
    created_at: datetime

    class Config:
        from_attributes = True


class ChatWithMessages(ChatOut):
    messages: List[MessageOut]