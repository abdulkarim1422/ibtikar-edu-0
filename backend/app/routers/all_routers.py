from fastapi import APIRouter, Request, Query
from app.routers import question

router = APIRouter()

router.include_router(question.router)

@router.get("/")
def read_root():
    return {"Hello": "World"}

