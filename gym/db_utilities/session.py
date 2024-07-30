from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from gym.config import DB_CONNECTION_URL


class GymSession:
    engine = create_engine(DB_CONNECTION_URL)

    @classmethod
    def get_session(cls):
        session_class = sessionmaker(bind=cls.engine)
        session = session_class()
        return session
