from gym.datamodel.booking import Booking
from gym.db_utilities import GymSession
from gym.crud.booking_update_crud import add_finished_status_by_booking


def add_new_booking(name):
    with GymSession.get_session() as session:
        booking = Booking(name=name)
        session.add(booking)
        session.commit()


def get_booking_by_name(name):
    with GymSession.get_session() as session:
        booking = session.query(Booking)\
            .filter(Booking.name == name)\
            .first()
        return booking


def make_booking_finished(name):
    booking = get_booking_by_name(name)
    if not booking:
        print(f'No such client in the database: {name}')
        return

    add_finished_status_by_booking(booking)
