from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser(
        prog='HellGymOperations',
        description='Take a look at SQLAlchemy through the prism of a useless project!',
        epilog='Make a choice already!'
    )
    parser.add_argument('-p', '--prefill', action='store_true', help='Prefill the database.')
    arguments = parser.parse_args()
    return arguments
