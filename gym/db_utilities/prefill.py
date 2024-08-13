from gym.datamodel import Booking, BookingUpdate, Trainer
from .session import GymSession


def prefill_database():
    with GymSession.get_session() as session:
        trainer_a = Trainer(name='Gigachad')
        session.add(trainer_a)
        session.commit()

        trainer_b = Trainer(name='Coach Potato')
        session.add(trainer_b)
        session.commit()

        booking_a = Booking()
        session.add(booking_a)
        session.commit()

        booking_b = Booking(name='Mr. Fancy Pants')
        session.add(booking_b)
        session.commit()

        update_a = BookingUpdate(booking_id=booking_a.id, trainer_id=trainer_a.id)
        session.add(update_a)
        session.commit()
