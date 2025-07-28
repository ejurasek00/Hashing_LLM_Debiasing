from collections import Counter
import pandas as pd
import datasets as ds
from mlxtend.frequent_patterns import apriori
from collections import Counter

def process_itemset(itemset):
    # Convert frozenset to sorted list of items
    return sorted(list(itemset))

def golden_itemsets(length, data):
    # Step 1: Load the data into a DataFrame
    df = pd.DataFrame(data)

    # Step 2: Separate categorical and numerical columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    numerical_cols = df.select_dtypes(include=['number']).columns

    # Step 3: Apply One-Hot Encoding to categorical columns
    one_hot_df = pd.get_dummies(df[categorical_cols], drop_first=False)
    
    # Step 4: Convert numerical columns to one-hot encoded format
    for col in numerical_cols:
        # Create a one-hot encoded column for each unique value in the numerical column
        for unique_val in df[col].unique():
            one_hot_df[f"{col}_{unique_val}"] = (df[col] == unique_val)

    # Step 5: Ensure all columns are boolean type
    one_hot_df = one_hot_df.astype(bool)

    one_hot_df.columns = [col.split('_')[-1] for col in one_hot_df.columns]
    # Step 6: Apply the Apriori algorithm with min_support = 0.5
    frequent_itemsets = apriori(one_hot_df, min_support=0.5, use_colnames=True)

    # Step 7: Filter itemsets to only include those of the specified length
    itemsets = frequent_itemsets[frequent_itemsets['itemsets'].apply(len) == length]

    # Convert to sets and return the result
    sorted_itemsets = [process_itemset(item) for item in itemsets['itemsets']]
    set_list = [set(item) for item in sorted_itemsets]

    # Print output for debugging
    #print("Column Names:", one_hot_df.columns.tolist())
    #print(type(set_list[0]) if set_list else "No sets found")
    #print(set_list)
    
    return set_list
        
def parse_custom_set(input_list):
    # Convert a list of sets into a list of sorted tuples
    return [tuple(sorted(s)) for s in input_list]


def compare_sets(set1, set_gold):
    # Parse the sets
    set1_converted = parse_custom_set(set1)
    set_gold_converted = parse_custom_set(set_gold)

    # Count the occurrences of each set in set1
    set1_counter = Counter(set1_converted)

    # Convert list to set for comparison
    set1_converted_set = set(set1_converted)
    set_gold_converted_set = set(set_gold_converted)
    print('_________________')
    print('Set gold:')
    print(set_gold)
    print('Set1:')
    print(set1)
    print('Lengths:')
    print('LLM generated number of items:')
    print(len(set1_converted_set))
    print('Golden number of items:')
    print(len(set_gold_converted_set))

    # Compute the intersection
    intersection = set1_converted_set.intersection(set_gold_converted_set)
    print('intersection count:')
    print(len(intersection))

    # Find hallucinations (in set1 but not in set_gold)
    hallucinations = set1_converted_set.difference(set_gold_converted_set)
    print('hallucination count:')
    print(len(hallucinations))

    # Find missing (in set_gold but not in set1)
    missing = set_gold_converted_set.difference(set1_converted_set)

    # Print the intersection
    '''
    print('---------------------------------------------------------------')
    print(set_gold)
    print(set1)
    print("Intersection:")
    for s in intersection:
        print(s)
    hallucination_count = 0
    # Print hallucinations
    if hallucinations:
        print("\nHallucinations:")
        for hallucination in hallucinations:
            hallucination_count+= 1
            print(hallucination)
    else:
        print("\nNo Hallucinations")
    print('Count of hallucinations: ' + '\n')
    print(hallucination_count)
    # Print missing
    if missing:
        print("\nMissing:")
        for miss in missing:
            print(miss)
    else:
        print("\nNo Missing")

    # Print duplicates
    duplicates = [item for item, count in set1_counter.items() if count > 1]

    if duplicates:
        print("\nDuplicates in set1:")
        for duplicate in duplicates:
            print(f"{duplicate} occurs {set1_counter[duplicate]} times")
    else:
        print("\nNo Duplicates in set1")
    '''


golden_itemsets(2,ds.correct)