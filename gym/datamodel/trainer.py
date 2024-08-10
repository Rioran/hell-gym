from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from .model_base import SqlAlchemyBase


class Trainer(SqlAlchemyBase):
    __tablename__ = 'trainers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    bio: Mapped[Optional[str]]
    created: Mapped[datetime] = mapped_column(server_default=func.now())

    updates: Mapped['BookingUpdate'] = relationship(back_populates='trainer')

    def __repr__(self):
        return f'<Trainer {self.id}: "{self.name}">'
