from gym.datamodel.booking import Booking
from gym.datamodel.booking_update import BookingUpdate
from gym.db_utilities import GymSession


def add_finished_status_by_booking(booking_object):
    with GymSession.get_session() as session:
        query = session.query(Booking).filter(Booking.id == booking_object.id)
        booking = query.first()
        updates = booking.updates
        if len(updates) != 1:
            print(f'Incorrect status, cannot make him finished')
            return

        update_with_start = updates[0]
        trainer_id = update_with_start.trainer_id
        new_update = BookingUpdate(trainer_id=trainer_id, booking_id=booking.id, status='finished')
        session.add(new_update)
        session.commit()
        print(f'Booking <{booking.name}> recieved status "finished"')
