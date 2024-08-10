from gym.datamodel import Booking, BookingUpdate, Trainer
from .session import GymSession


def prefill_database():
    with GymSession.get_session() as session:
        trainer_a = Trainer(name='Gigachad')
        trainer_b = Trainer(name='Coach Potato')
        booking_a = Booking()
        booking_b = Booking(name='Mr. Fancy Pants')
        update_a = BookingUpdate(booking_id=booking_a.id, trainer_id=trainer_a.id)
        all_items = [trainer_a, trainer_b, booking_a, booking_b, update_a]
        session.add_all(all_items)
        session.commit()
