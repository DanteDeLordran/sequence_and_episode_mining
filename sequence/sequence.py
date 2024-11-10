import pandas as pd
import itertools
from tkinter import filedialog

# Load the CSV data into a pandas dataframe
data = pd.read_csv( filedialog.askopenfilename(), header=None, names=["Items"], sep=None, engine='python', dtype=str)

# Preprocess the data: convert each row of items to a list
transactions = data['Items'].str.split(',')

# Function to generate candidate itemsets of a given size
def generate_candidates(itemsets, size):
    candidates = []
    for itemset1 in itemsets:
        for itemset2 in itemsets:
            candidate = set(itemset1).union(set(itemset2))
            if len(candidate) == size:
                candidates.append(frozenset(candidate))
    return candidates

# Function to calculate support count of an itemset in the transactions
def support_count(itemset, transactions):
    return sum(1 for transaction in transactions if itemset.issubset(transaction))

# Apriori Algorithm Implementation
def apriori(transactions, min_support):
    itemsets = [frozenset([item]) for transaction in transactions for item in transaction]
    itemsets = list(set(itemsets))  # Remove duplicates

    frequent_itemsets = []
    candidate_itemsets = itemsets
    k = 1

    while candidate_itemsets:
        # Calculate support count for each candidate itemset
        itemset_support = {itemset: support_count(itemset, transactions) for itemset in candidate_itemsets}

        # Filter itemsets that meet the minimum support
        frequent_itemsets_k = {itemset: support for itemset, support in itemset_support.items() if support >= min_support}

        # Add frequent itemsets of size k to the final list
        frequent_itemsets.extend(frequent_itemsets_k.items())

        # Generate candidate itemsets for next size k+1
        candidate_itemsets = generate_candidates(list(frequent_itemsets_k.keys()), k + 1)
        k += 1

    return frequent_itemsets

# Minimum support threshold (example: 2 transactions)
min_support = 2

# Apply Apriori Algorithm
frequent_itemsets = apriori(transactions, min_support)

# Display the frequent itemsets with their counts
print("Frequent Itemsets with Counts:")
for itemset, count in frequent_itemsets:
    print(f"Itemset: {itemset}, Count: {count}")
