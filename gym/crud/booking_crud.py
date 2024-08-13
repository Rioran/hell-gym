from gym.datamodel.booking import Booking
from gym.db_utilities import GymSession


def create_new_booking(name):
    with GymSession.get_session() as session:
        booker_name = Booking(name=name)
        all_items = [booker_name]
        session.add_all(all_items)
        session.commit()
