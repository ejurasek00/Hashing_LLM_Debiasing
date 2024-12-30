In this folder you find python functionality to compare golden (Apriori) generated itemsets with LLM generated itemsets.
You can find Several files in this directory:
The txt files store modified LLM outputs. The type of output is in the name of the file: type_LLM.txt where type is 
(correct, hashed or wrong) and LLM represent of what LLM the answers are.
The executable file is the main.py file which handles what datasets should be compared and the txt files handling.
The functions.py file contains functions used by the main.py. It handles the Apriori algorythm and itemset comparison.
The dataset.py contains golden datasets stored as dictionary.