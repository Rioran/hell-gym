from gym.datamodel import Trainer
from gym.db_utilities import GymSession
from gym.config import PRINT_ITEMS_PER_PAGE


def get_recent_trainers(limit=PRINT_ITEMS_PER_PAGE, offset=0):
    with GymSession.get_session() as session:
        query = session.query(Trainer).order_by(Trainer.id)
        if limit:
            query = query.limit(limit).offset(offset)
        data = query.all()
    return data


def add_new_trainer(trainer_name, trainer_bio='Not filled'):
    with GymSession.get_session() as session:
        name = Trainer(name=trainer_name)
        bio = Trainer(bio=trainer_bio)
        all_items = [name, bio]
        session.add_all(all_items)
        session.commit()
