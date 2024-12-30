from collections import Counter
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from collections import Counter
import functions
import datasets as ds
import ast
from collections import Counter

# Assume functions.golden_itemsets and functions.compare_sets are already defined somewhere in your code.
# Here, I will assume they're part of a module `functions`, which is imported for use.

def parse_line_to_set(line):
    """
    Extract the sets from the line as strings, keeping their original format.
    """
    return line.strip()

def split_file_into_groups(file_path):
    """
    Split the file into groups based on the "CORRECT LENGTH" labels and extract the sets from each group.
    """
    groups = {1: [], 2: [], 3: [], 4: [], 5: []}
    current_length = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespaces
            
            # If line starts with "LENGTH", extract the group number
            if line.startswith("LENGTH"):
                current_length = int(line.split()[-1])  # Get the number after "CORRECT LENGTH"
            elif line and current_length is not None:
                # Add the line to the corresponding group
                groups[current_length].append(parse_line_to_set(line))
    
    return groups

# Define the function that will iterate through the groups and execute the provided functions.
def execute_functions_for_groups(file_path):
    # First, split the file into groups
    groups = split_file_into_groups(file_path)
    
    # Now, iterate through each group and its sets
    for length, sets_group in groups.items():
        print(f"\nProcessing Group {length} sets:")
        print('-----------------------------------------------------------')
        
        # Generate the golden set for the current length
        golden_set = functions.golden_itemsets(length, ds.wrong)
        
        # Iterate over each set in the current group
        for set_str in sets_group:
            # Convert the string back to a set (assuming set_str is a string like '[{"2"},{"4"},{"herbivore"}]')
            current_set = eval(set_str)  # Evaluating the string to convert it back to a set
            
            # Call the compare_sets function with the current set and the golden set
            functions.compare_sets(current_set, golden_set)

# Example usage
file_path = 'wrong_gpt.txt'  # Replace with your actual file path
print(f'Evalueating {file_path}: __________________')
execute_functions_for_groups(file_path)

