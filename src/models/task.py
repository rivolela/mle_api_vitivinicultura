from fastapi import FastAPI
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
