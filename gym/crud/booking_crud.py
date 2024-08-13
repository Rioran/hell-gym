from gym.datamodel.booking import Booking
from gym.db_utilities import GymSession


def create_new_booking(name):
    with GymSession.get_session() as session:
        booking = Booking(name=name)
        session.add(booking)
        session.commit()
