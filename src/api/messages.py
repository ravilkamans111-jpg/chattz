from sys import prefix

from fastapi import APIRouter, Depends, HTTPException, Query, status

from src.crud.messages import create_message
from src.crud.chats import get_chat

from src.database import SessionDep
from src.schemas.messages import MessageCreate

router = APIRouter(prefix='/messages')

@router.post(
    "/{chat_id}/messages/")
async def send_message(
    chat_id: int,
    data: MessageCreate,
    session: SessionDep
):
    chat = await get_chat(session, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    return await create_message(session, chat, data.text)