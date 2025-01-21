from fastapi import APIRouter, Request, Query

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

