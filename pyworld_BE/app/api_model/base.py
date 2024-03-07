from typing import Annotated

from annotated_types import Ge
from pydantic import AfterValidator, BaseModel, ConfigDict


def ts_si_down(ts: int):
    return ts * 1000


SecToMilliSecTs = Annotated[int, Ge(0), AfterValidator(ts_si_down)]


class OrmBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
