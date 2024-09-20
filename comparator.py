# Comparator.py

from collections import Counter


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

    # Compute the intersection
    intersection = set1_converted_set.intersection(set_gold_converted_set)

    # Find hallucinations (in set1 but not in set_gold)
    hallucinations = set1_converted_set.difference(set_gold_converted_set)

    # Find missing (in set_gold but not in set1)
    missing = set_gold_converted_set.difference(set1_converted_set)

    # Print the intersection
    print("Intersection:")
    for s in intersection:
        print(s)

    # Print hallucinations
    if hallucinations:
        print("\nHallucinations:")
        for hallucination in hallucinations:
            print(hallucination)
    else:
        print("\nNo Hallucinations")

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


# Compare sets
set1 = [{"1", "2", "3"}, {"2", "3", "1"}, {"7", "8", "9"}, ]
set_gold = [{"3", "2", "1"}, {"6", "5", "4"}]
compare_sets(set1, set_gold)

"""
# Example usage:

# Compare sets
set1 = [{"1", "2", "3"},{"2","3","1"},{"7", "8", "9"}, ]
set_gold = [{"3", "2", "1"}, {"6", "5", "4"}]
compare_sets(set1, set_gold)
"""
