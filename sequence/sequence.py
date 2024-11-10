import csv
from collections import defaultdict


def load_sequences_from_csv(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            sequences.append(row)
    return sequences


def generate_candidates(prev_patterns, length):
    candidates = []
    for i in range(len(prev_patterns)):
        for j in range(len(prev_patterns)):

            if prev_patterns[i][1:] == prev_patterns[j][:-1]:
                candidates.append(prev_patterns[i] + [prev_patterns[j][-1]])
    return candidates


def count_support(sequences, pattern):
    count = 0
    for sequence in sequences:
        seq_index = 0
        for item in pattern:

            if item in sequence[seq_index:]:
                seq_index = sequence.index(item, seq_index) + 1
            else:
                break
        else:
            count += 1
    return count


def apriori_sequence_mining(sequences, minsup):
    patterns = []

    single_items = {item for sequence in sequences for item in sequence}
    current_patterns = [[item] for item in single_items]

    while current_patterns:

        next_patterns = []
        for pattern in current_patterns:
            support = count_support(sequences, pattern)
            if support / len(sequences) >= minsup:
                patterns.append(pattern)
                next_patterns.append(pattern)

        current_patterns = generate_candidates(next_patterns, len(next_patterns[0]) + 1) if next_patterns else []

    return patterns


def run():
    file_path = '../sample_two.csv'
    minsup = 0.1
    sequences = load_sequences_from_csv(file_path)
    frequent_patterns = apriori_sequence_mining(sequences, minsup)
    print("Frequent sequential patterns:", frequent_patterns)


if __name__ == '__main__':
    run()