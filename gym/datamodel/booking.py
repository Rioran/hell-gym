from sqlalchemy.orm import Mapped, mapped_column

from model_base import SqlAlchemyBase


class Booking(SqlAlchemyBase):
    __tablename__ = 'bookings'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(default='Average Joe')

    def __repr__(self):
        return f'<Booking {self.id}: "{self.name}">'
