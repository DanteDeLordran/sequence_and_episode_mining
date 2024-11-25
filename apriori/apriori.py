import csv
from itertools import combinations
from tkinter import filedialog


def load_transactions_from_csv(file_path):
    transactions = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            transactions.append(set(row))
    return transactions


def apriori(transactions, minsup):
    def get_frequent_item_sets(itemsets, minsup, transaction_count):
        itemset_counts = {}
        for transaction in transactions:
            for itemset in itemsets:
                if itemset.issubset(transaction):
                    itemset_counts[itemset] = itemset_counts.get(itemset, 0) + 1
        return {itemset for itemset, count in itemset_counts.items() if count / transaction_count >= minsup}, itemset_counts

    def generate_candidates(prev_frequent_itemsets, k):
        candidates = set()
        prev_list = list(prev_frequent_itemsets)
        for i in range(len(prev_list)):
            for j in range(i + 1, len(prev_list)):
                union = prev_list[i] | prev_list[j]
                if len(union) == k + 1:
                    if all(frozenset(subset) in prev_frequent_itemsets for subset in combinations(union, k)):
                        candidates.add(union)
        return candidates

    transaction_count = len(transactions)
    itemsets = {frozenset([item]) for transaction in transactions for item in transaction}
    frequent_itemsets = []
    k = 1

    while True:
        current_frequent_itemsets, itemset_counts = get_frequent_item_sets(itemsets, minsup, transaction_count)
        if not current_frequent_itemsets:
            break

        frequent_itemsets.extend(current_frequent_itemsets)

        itemsets = generate_candidates(current_frequent_itemsets, k)
        k += 1

    return frequent_itemsets


def run():
    file_path = filedialog.askopenfilename()
    minsup = 0.1

    transactions = load_transactions_from_csv(file_path)

    frequent_item_sets = apriori(transactions, minsup)

    # Save results to a text file
    with open('frequent_item_sets.txt', 'w') as file:
        file.write("Frequent item sets:\n")
        for itemset in frequent_item_sets:
            file.write(f"{set(itemset)}\n")

    print("Frequent item sets have been saved to 'frequent_item_sets.txt'.")


if __name__ == '__main__':
    run()
