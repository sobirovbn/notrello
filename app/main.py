from typing import Union
from fastapi import FastAPI
import uvicorn

from app.user.views import router as users_router
from app.task.views import router as task_router
from app.board.views import router as boards_router


app = FastAPI()
app.include_router(users_router)
app.include_router(boards_router)
app.include_router(task_router)

if __name__ == '__main__': 
    uvicorn.run("main:app", reload=True)
