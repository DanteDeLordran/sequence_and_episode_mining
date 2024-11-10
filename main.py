from episode.episode import episodes
from utils.utils import get_csv_as_matrix


def main():
    matrix = get_csv_as_matrix()
    episodes(matrix)


if __name__ == '__main__':
    main()