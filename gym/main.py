from .arguments import parse_arguments
from .db_utilities import prefill_database, reset_db, setup_db


def main():
    arguments = parse_arguments()

    #if arguments.prefill:
    #    reset_db()

    setup_db()

    if arguments.prefill:
        prefill_database()


if __name__ == '__main__':
    main()
