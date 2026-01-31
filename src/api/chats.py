from fastapi import APIRouter, Depends, HTTPException, Query, status

from src.crud.messages import get_last_messages
from src.database import SessionDep
from src.schemas.chats import ChatOut, ChatCreate, ChatWithMessages

router = APIRouter(prefix='/chats')

@router.post("/", response_model=ChatOut)
async def create_chat(data: ChatCreate, session: SessionDep):
    return await create_chat(session, data.title)

@router.get(
    "/{chat_id}",
    response_model=ChatWithMessages
)
async def get_chat(
    chat_id: int,
    session: SessionDep,
    limit: int = Query(20, ge=1, le=100)
):
    chat = await get_chat(session, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    messages = await get_last_messages(session, chat_id, limit)
    return {**chat.__dict__, "messages": messages}


@router.delete(
    "/{chat_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_chat(chat_id: int, session: SessionDep):
    chat = await get_chat(session, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    await session.delete(chat)
    await session.commit()