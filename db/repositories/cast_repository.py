import json
from typing import Optional

from db.dto.cast_dto import CastDto
from db.models import Cast
from db.repositories.base_repository import BaseRepository


class CastRepository(BaseRepository):
    def get(self,
            id_: Optional[int] = None,
            name: Optional[str] = None,
            db=None
            ) -> Optional[CastDto]:
        conditions = []
        if id_:
            conditions.append(Cast.id == id_)
        if name:
            conditions.append(Cast.full_name == name)
        record = db.session.query(Cast).filter(
            *conditions
        ).first()
        return CastDto(
            id=record.id,
            full_name=record.full_name,
            image_url=record.image_url,
            movie_names=json.loads(record.movie_names) if record.movie_names else []
        ) if record else None

    def add_update(self, name: str, movie_name: Optional[str] = None,
                   image_url: Optional[str] = None, db=None):
        record = db.session.query(Cast).filter(Cast.full_name == name).first()
        if record:
            existing_movie_names = json.loads(record.movie_names) if record.movie_names else []
            if movie_name is not None and movie_name not in existing_movie_names:
                existing_movie_names.append(movie_name)
            record.movie_names = json.dumps(existing_movie_names)
        else:
            movie_names_json = json.dumps([movie_name]) if movie_name else json.dumps([])
            record = Cast(
                full_name=name,
                movie_names=movie_names_json,
                image_url=image_url
            )
            db.session.add(record)
        db.session.flush()
        record_id = record.id
        db.session.commit()
        return record_id
