import uvicorn
from fastapi import FastAPI
from src.api.chats import router as chats_router
from src.api.messages import router as message_router

app = FastAPI(title="Chat API")

app.include_router(router = chats_router)
app.include_router(router = message_router)

