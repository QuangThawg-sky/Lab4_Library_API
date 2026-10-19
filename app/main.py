
from fastapi import FastAPI

from app.routers import books

app = FastAPI(
    title="Library API",
    description="Web API CRUD quản lý sách",
    version="1.0.0",
)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}


app.include_router(books.router)
