from fastapi import APIRouter


messages = APIRouter(prefix="/messages", tags=["Messages"])
