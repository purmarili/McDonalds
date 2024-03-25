from typing import Optional

from pydantic import BaseModel


class CastDto(BaseModel):
    id: int
    full_name: str
    movie_names: Optional[list[str]]
    image_url: Optional[str]
