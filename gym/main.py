from arguments import handle_arguments
from db_utilities import setup_db


def main():
    setup_db()
    handle_arguments()


if __name__ == '__main__':
    main()
