from gym.datamodel import Trainer
from gym.db_utilities.session import GymSession


def add_new_trainer(trainer_name, trainer_bio='Not filled'):
    with GymSession.get_session() as session:
        name = Trainer(name=trainer_name)
        bio = Trainer(bio=trainer_bio)
        all_items = [name, bio]
        session.add_all(all_items)
        session.commit()
