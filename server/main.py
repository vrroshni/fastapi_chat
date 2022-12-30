from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union
import requests


app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credenttials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PROJECT_ID=""
PRIVATE_KEY=""


class User(BaseModel):
    username: str
    secret: str
    email: Union[str, None] = None
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None