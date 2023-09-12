from fastapi import FastAPI

from routes.routes import todo_router

app = FastAPI()
app.include_router(todo_router)


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}