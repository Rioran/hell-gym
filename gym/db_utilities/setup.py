from gym.datamodel import SqlAlchemyBase
from .session import GymSession


def reset_db():
    SqlAlchemyBase.metadata.drop_all(GymSession.engine)


def setup_db():
    SqlAlchemyBase.metadata.create_all(GymSession.engine)
