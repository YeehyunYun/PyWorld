from app import hello
from base.app import app


app.include_router(hello.ROUTER, prefix="/hello")
