from gym.datamodel import SqlAlchemyBase


def print_entries(entries: list[SqlAlchemyBase]):
    print(f'{type(entries[0])} - {len(entries)} items:')
    for item in entries:
        print(f'\t{item}')
