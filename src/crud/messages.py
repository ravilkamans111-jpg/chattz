from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.chats import Chat
from src.models.messages import Message


async def create_message(
    session: AsyncSession, chat: Chat, text: str
) -> Message:
    message = Message(chat_id=chat.id, text=text)
    session.add(message)
    await session.commit()
    await session.refresh(message)
    return message


async def get_last_messages(
    session: AsyncSession, chat_id: int, limit: int
):
    result = await session.execute(
        select(Message)
        .where(Message.chat_id == chat_id)
        .order_by(Message.created_at.desc())
        .limit(limit)
    )
    return list(reversed(result.scalars().all()))