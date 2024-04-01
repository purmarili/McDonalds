import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserOrderDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: Optional[int] = None
    details: Optional[str] = None
    date: Optional[datetime.datetime] = None
    preparation_time: Optional[int] = None
