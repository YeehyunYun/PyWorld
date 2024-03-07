import sqlalchemy as sa
import sqlalchemy.orm as sao

from base import OrmBaseModel, SecToMilliSecTs


class Borad(OrmBaseModel):
    id: int
    title: str
    content: str
    created: SecToMilliSecTs
