from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser(
        prog='HellGymOperations',
        description='Take a look at SQLAlchemy through the prism of a useless project!',
        epilog='Make a choice already!'
    )
    # Add a mutually exclusive group to ensure --register-trainer and --prefill cant be used together
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-p', '--prefill', action='store_true', help='Prefill the database.')
    parser.add_argument('-t', '--trainers', action='store_true', help='See latest trainers.')
    group.add_argument('--register-trainer', nargs='+', metavar=('trainer_name', 'trainer_bio'), help='Register a new trainer with optional bio.')
    parser.add_argument('-nb', '--new-booking', action='store_true', help='Add new booking.')
    arguments = parser.parse_args()
    return arguments
