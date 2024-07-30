from sqlalchemy.orm import Mapped, mapped_column

from model_base import SqlAlchemyBase


class Trainer(SqlAlchemyBase):
    __tablename__ = 'trainers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(default='Average Joe')

    def __repr__(self):
        return f'<Trainer {self.id}: "{self.name}">'
