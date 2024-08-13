from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser(
        prog='HellGymOperations',
        description='Take a look at SQLAlchemy through the prism of a useless project!',
        epilog='Make a choice already!'
    )
    parser.add_argument('-p', '--prefill', action='store_true', help='Prefill the database.')
    parser.add_argument('-t', '--trainers', action='store_true', help='See latest trainers.')
    parser.add_argument('-nb', '--new-booking', action='store_true', help='Add new booking.')

    arguments = parser.parse_args()
    return arguments
