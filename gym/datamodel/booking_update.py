from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from .model_base import SqlAlchemyBase


class BookingUpdate(SqlAlchemyBase):
    __tablename__ = 'booking_updates'

    id: Mapped[int] = mapped_column(primary_key=True)
    booking_id: Mapped[Optional[int]] = mapped_column(ForeignKey('bookings.id'))
    trainer_id: Mapped[Optional[int]] = mapped_column(ForeignKey('trainers.id'))

    booking: Mapped['Booking'] = relationship(back_populates='updates')
    trainer: Mapped['Trainer'] = relationship(back_populates='updates')

    status: Mapped[str] = mapped_column(default='started')
    created: Mapped[datetime] = mapped_column(server_default=func.now())

    def __repr__(self):
        return f'<Booking update {self.id}: {self.booking.name} {self.status} with {self.trainer.name}>'
