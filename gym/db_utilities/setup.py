from gym.datamodel.model_base import SqlAlchemyBase
from gym.db_utilities.session import GymSession


def setup_db():
    SqlAlchemyBase.metadata.create_all(GymSession.engine)
