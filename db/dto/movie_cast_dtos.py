from pydantic import BaseModel

from db.dto.cast_dto import CastDto


class CastByMovieDto(BaseModel):
    id: int
    movie_id: int
    movie_name: str
    cast: list[CastDto]
