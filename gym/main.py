from .arguments import parse_arguments
from .crud.trainer_crud import get_recent_trainers
from .db_utilities import prefill_database, print_entries, reset_db, setup_db


def main():
    arguments = parse_arguments()

    if arguments.prefill:
        reset_db()
    setup_db()
    if arguments.prefill:
        prefill_database()

    if arguments.trainers:
        trainers = get_recent_trainers()
        print_entries(trainers)


if __name__ == '__main__':
    main()
