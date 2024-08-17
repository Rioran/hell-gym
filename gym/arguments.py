from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser(
        prog='HellGymOperations',
        description='Take a look at SQLAlchemy through the prism of a useless project!',
        epilog='Make a choice already!'
    )
    parser.add_argument('-t', '--trainers', action='store_true', help='See latest trainers.')
    parser.add_argument('-b', '--bookings', action='store_true', help='See latest bookings.')
    parser.add_argument('-u', '--updates', action='store_true', help='See latest booking updates.')
    
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-p', '--prefill', action='store_true', help='Prefill the database.')
    group.add_argument(
        '-rt', '--register-trainer',
        nargs='+',
        metavar=('trainer_name', 'trainer_bio'),
        help='Register a new trainer with optional bio.'
    )
    group.add_argument(
        '-fc', '--finish-client',
        metavar='client_name',
        help='Add status "finished" to specified client if possible.'
    )
    group.add_argument(
        '-a', '--ask-for-client',
        metavar='trainer_name',
        type=str,
        help='Add a client if there is one for a specific trainer (specify the trainer name).'
    )
    group.add_argument(
        '-nb', '--new-booking',
        metavar='booking_name',
        help='Add new booking, name must be specified.'
    )
    
    arguments = parser.parse_args()
    return arguments
