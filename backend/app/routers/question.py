from fastapi import APIRouter, Request, Query
from app.services import question

router = APIRouter()

@router.get("/zero_exam_loop")
def zero_exam_loop():
    return question.zero_exam_loop()


