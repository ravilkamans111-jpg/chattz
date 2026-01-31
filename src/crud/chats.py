from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.chats import Chat

async def create_chat(session: AsyncSession, title: str) -> Chat:
    chat = Chat(title=title)
    session.add(chat)
    await session.commit()
    await session.refresh(chat)
    return chat


async def get_chat(session: AsyncSession, chat_id: int) -> Chat | None:
    result = await session.execute(
        select(Chat).where(Chat.id == chat_id)
    )
    return result.scalar_one_or_none()