from typing import List

from db.dto.movie_dto import MovieDto
from db.models import Movie
from db.repositories.base_repository import BaseRepository


class MovieRepository(BaseRepository):

    def get(self, id_: int, title: str = None, year: int = None, db=None) -> List[MovieDto]:
        conditions = []
        if id_:
            conditions.append(Movie.id == id_)
        if title:
            conditions.append(Movie.title == title)
        if year:
            conditions.append(Movie.year == year)

        results = db.session.query(Movie).filter(*conditions).all()
        return [
            MovieDto(
                title=title,
                year=r.year,
                time=r.time,
                rating=r.rating,
                rating_count=r.rating_count,
                top_250_rating=r.top_250_rating,
                image_url=r.image_url
            )
            for r in results
        ]

    def add(self, title: str, year: int, time: str, rating: float,
            rating_count: str, top_250_rating: int, image_url: str, db):
        result = db.session.query(Movie).filter(
            Movie.title == title, Movie.year == year
        ).first()
        if result:
            return result.id
        result = Movie(
            title=title,
            year=year,
            time=time,
            rating=rating,
            rating_count=rating_count,
            top_250_rating=top_250_rating,
            image_url=image_url
        )
        db.session.add(result)
        db.session.flush()
        result_id = result.id
        db.session.commit()
        return result_id

    def delete(self, id_: int, db):
        order = db.session.query(Movie).filter(
            Movie.id == id_
        ).one_or_none()
        db.session.delete(order)
        db.session.commit()
