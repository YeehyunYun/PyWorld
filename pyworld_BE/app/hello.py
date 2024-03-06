from __future__ import annotations

from fastapi import APIRouter


ROUTER = APIRouter()


@ROUTER.get("/")
def get_hello():
    return {"Hello": "World"}
