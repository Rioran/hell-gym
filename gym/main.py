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

    if arguments.ask_for_client:
        trainer_name = arguments.ask_for_client
        trainer = get_trainer_by_name(trainer_name)
        if trainer:
            client = get_client()  # You need to implement this function
            if client:
                add_client_to_trainer(trainer, client)
            else:
                print("No client available to add to the trainer.")
        else:
            print(f"No trainer found with the name {trainer_name}")

if __name__ == '__main__':
    main()
