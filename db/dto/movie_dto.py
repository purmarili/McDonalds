from typing import Optional

from pydantic import BaseModel


class MovieDto(BaseModel):
    title: Optional[str] = None
    year: Optional[int] = None
    time: Optional[str] = None
    rating: Optional[float] = None
    rating_count: Optional[str] = None
    top_250_rating: Optional[int] = None
    image_url: Optional[str] = None

    def __str__(self):
        return (f'{self.time}, ({self.year}), {self.time}, {self.rating},'
                f'{self.rating_count}, {self.top_250_rating}')
