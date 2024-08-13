from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser(
        prog='HellGymOperations',
        description='Take a look at SQLAlchemy through the prism of a useless project!',
        epilog='Make a choice already!'
    )
    parser.add_argument('-p', '--prefill', action='store_true', help='Prefill the database.')
    parser.add_argument('-t', '--trainers', action='store_true', help='See latest trainers.')
    parser.add_argument('-fc', '--finish-client', metavar='trainer_name', help='Finish client for a specified trainer.')
    parser.add_argument(
        '-a', '--ask-for-client',
        metavar='trainer_name',
        type=str,
        help='Add a client if there is one for a specific trainer (specify the trainer name).'
    )
    parser.add_argument(
        '-nb', '--new-booking',
        metavar='booking_name',
        help='Add new booking, name must be specified.'
    )
    
    arguments = parser.parse_args()
    return arguments
