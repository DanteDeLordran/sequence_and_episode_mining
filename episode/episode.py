import csv
from tkinter import filedialog


def load_episodes_from_csv(file_path):
    """Load episodes from a CSV file, treating columns as sequences."""
    episodes = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        # Transpose rows into columns to treat columns as sequences
        episodes = [[row[i] for row in rows if i < len(row)] for i in range(len(rows[0]))]
    return episodes


def generate_candidates(prev_patterns, length):
    """Generate candidate patterns by joining previous patterns."""
    candidates = []
    for i in range(len(prev_patterns)):
        for j in range(len(prev_patterns)):
            if prev_patterns[i][1:] == prev_patterns[j][:-1]:
                candidates.append(prev_patterns[i] + [prev_patterns[j][-1]])
    return candidates


def count_support(sequences, pattern):
    """Count the support of a pattern in the sequences."""
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
    """Perform Apriori-based sequence mining on the sequences."""
    patterns = []

    # Get single items as initial patterns
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
    """Run the episode mining process."""
    file_path = filedialog.askopenfilename()
    minsup = 0.8
    sequences = load_episodes_from_csv(file_path)
    frequent_patterns = apriori_sequence_mining(sequences, minsup)

    print("Frequent sequential patterns:", frequent_patterns)
    with open('frequent_patterns.txt', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(frequent_patterns)


if __name__ == '__main__':
    run()
