from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from .model_base import SqlAlchemyBase


class Booking(SqlAlchemyBase):
    __tablename__ = 'bookings'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(default='Mr. Incognito')
    created: Mapped[datetime] = mapped_column(server_default=func.now())
    updates: Mapped[Optional[list['BookingUpdate']]] = relationship(back_populates='booking')

    def __repr__(self):
        return f'<Booking {self.id}: "{self.name}">'
