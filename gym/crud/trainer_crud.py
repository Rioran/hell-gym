from sqlalchemy import select

from gym.datamodel import Booking, BookingUpdate, Trainer
from gym.db_utilities import GymSession
from gym.config import PRINT_ITEMS_PER_PAGE


def get_recent_trainers(limit=PRINT_ITEMS_PER_PAGE, offset=0):
    with GymSession.get_session() as session:
        query = session.query(Trainer).order_by(Trainer.id)
        if limit:
            query = query.limit(limit).offset(offset)
        data = query.all()
    return data



def get_trainer_by_name(trainer_name):
    with GymSession.get_session() as session:
        trainer = session.query(Trainer).filter(Trainer.name == trainer_name).first()
        return trainer


def is_trainer_available(trainer_name):
    trainer = get_trainer_by_name(trainer_name)
    if trainer:
        return True
    return False

def get_unoccupied_client():
    with GymSession.get_session() as session:
        unoccupied_client = (
            session.query(Booking)
            .outerjoin(BookingUpdate)
            .filter(BookingUpdate.id == None)
            .order_by(Booking.id)
            .first()
        )
        return unoccupied_client

def add_new_trainer(trainer_name, trainer_bio='Not filled'):
    with GymSession.get_session() as session:
        new_trainer = Trainer(name=trainer_name, bio=trainer_bio)
        session.add(new_trainer)
        session.commit()

