from pyworld.pyworld_BE.app import board
from base.app import app


app.include_router(board.ROUTER, prefix="/board")
