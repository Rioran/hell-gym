from gym.datamodel import SqlAlchemyBase
from .session import GymSession


def setup_db():
    SqlAlchemyBase.metadata.create_all(GymSession.engine)
