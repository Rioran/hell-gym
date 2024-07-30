from sqlalchemy.orm import Mapped, mapped_column

from model_base import SqlAlchemyBase


class BookingUpdate(SqlAlchemyBase):
    __tablename__ = 'booking_updates'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(default='Average Joe')

    def __repr__(self):
        return f'<Booking update {self.id}: "{self.name}">'
