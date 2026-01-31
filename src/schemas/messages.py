from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class MessageCreate(BaseModel):
    text: str = Field(min_length=1, max_length=5000)

    def model_post_init(self, __context):
        self.text = self.text.strip()


class MessageOut(BaseModel):
    id: int
    text: str
    created_at: datetime

    class Config:
        from_attributes = True


