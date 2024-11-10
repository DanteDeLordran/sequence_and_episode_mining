import csv
from collections import defaultdict


def load_episodes_by_column(file_path):
    episodes = defaultdict(list)

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for episode, item in row.items():
                if item:
                    episodes[episode].append(item)

    return episodes


def run():
    file_path = '../sample_four.csv'

    episodes = load_episodes_by_column(file_path)

    for episode, items in episodes.items():
        print(f"{episode}: {items}")


if __name__ == '__main__':
    run()