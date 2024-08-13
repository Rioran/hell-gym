from .arguments import parse_arguments
from .crud import add_new_booking, add_new_trainer, get_recent_entries
from .datamodel import Booking, BookingUpdate, Trainer
from .db_utilities import prefill_database, print_entries, reset_db, setup_db


def main():
    arguments = parse_arguments()
    print(f'\n{arguments = }')
    print(f'{arguments.register_trainer = }')
    for item in dir(arguments):
        if item[0] != '_':
            print(f'\t{item}')

    if arguments.prefill:
        reset_db()
    setup_db()
    if arguments.prefill:
        prefill_database()

    if arguments.register_trainer:
        add_new_trainer(*arguments.register_trainer)

    if arguments.new_booking:
        add_new_booking(arguments.new_booking)

    if arguments.trainers:
        trainers = get_recent_entries(Trainer)
        print_entries(trainers)

    if arguments.bookings:
        bookings = get_recent_entries(Booking)
        print_entries(bookings)

    if arguments.updates:
        updates = get_recent_entries(BookingUpdate)
        print_entries(updates)


if __name__ == '__main__':
    main()
