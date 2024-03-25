from typing import Optional

from db.dto.cast_dto import CastDto
from db.dto.movie_cast_dtos import CastByMovieDto
from db.models import MovieCast, Cast, Movie
from db.repositories.base_repository import BaseRepository


class MovieCastRepository(BaseRepository):
    def get_by_movie(self, id_: Optional[int] = None, db=None) -> Optional[CastByMovieDto]:
        record = db.session.query(
            MovieCast, Cast, Movie
        ).join(
            Cast, Cast.id == MovieCast.cast_id
        ).join(
            Movie, Movie.id == MovieCast.movie_id
        ).filter(
            MovieCast.movie_id == id_
        ).all()
        return CastByMovieDto(
            id=record[0].MovieCast.id,
            movie_id=record[0].MovieCast.movie_id,
            movie_name=record[0].Movie.title,
            cast=[CastDto(
                id=r.Cast.id,
                full_name=r.Cast.full_name,
                movie_names=r.Cast.movie_names,
                image_url=r.Cast.image_url
            ) for r in record]
        ) if record else None

    def add(self, movie_id: int, cast_id: int, db):
        record = db.session.query(MovieCast).filter(
            MovieCast.movie_id == movie_id, MovieCast.cast_id == cast_id
        ).first()
        if record:
            return
        db.session.add(
            MovieCast(
                movie_id=movie_id,
                cast_id=cast_id
            )
        )
        db.session.commit()
