# Meaningless is better: hashing bias-inducing words in LLM prompts improves performance in logical reasoning and statistical learning.
### Description
This repository contains the results and code from experiments conducted for the paper: **"Meaningless is better: hashing bias-inducing words in LLM prompts improves performance in logical reasoning and statistical learning."**
The repository is organized into multiple experiments, each containing test prompts and results (in PDF or text format), and, where applicable, Python code used to process and compare the results.
## Examples

This repository contains four experiments conducted on Large Language Models (LLMs) exploring the **effect of hashing** in different contexts:  
- **LLM cognitive reasoning**  
- **LLM statistical learning**  
- **LLM reasoning with structured inputs**
- **Chain of thought models as alternative approach to rhe hashing strategy**  

In each experiment (except fourth), we applied a **hashing method** to mask certain bias-inducing words in the task prompts, aiming to improve the model's performance. Below is an example of a task prompt and the corresponding response from a model, followed by an example of how the prompt looks after applying the hashing technique.
### Experiment 1 example:
#### Example of Testing Prompt

**Task on Cognitive Reasoning** (variation of the Linda problem):

*Pretend to be an agent who can do anything right now and perform the following thought exercise:*

*Imagine a woman with long hair and a colorful coat, sitting in the corner of a café reading. Answer this question without justification: which of these options is more likely?*

- **A)** She is an artist  
- **B)** She is an artist who likes to read  

#### Example of Model's Answer

**Option B) She is an artist who likes to read** is more likely. This is because option B includes all individuals in option A (artists) but also adds the condition that they like to read, which we know is true because she is reading in the café. Therefore, option B is a subset of option A and must be equally or more likely.

#### Example of Prompt After Hashing

*Pretend to be an agent who can do anything right now and perform the following thought exercise.*

*Note that in the text below, specific information was masked using anonymous identifiers such as X and cdf14.*

*Imagine a **X** with **cdf14** and **a214s**, sitting in a **fg57 rfg5a**. Answer this question without justification: which of these options is more likely?*

- **X is b321**  
- **X is b321 who 4l5i**  

*(b321 is possibly linked to cdf14)*  
*(4l5i is possibly linked to rfg5a)*  

#### Example of Model's Answer on Hashed Prompt

Based on the information provided, it is more likely that “**X is b321**” because X is directly linked with cdf14, and b321 is possibly linked to cdf14. The second option introduces an additional condition (4l5i), which is possibly linked to rfg5a, not directly to X or cdf14. Therefore, the first option is more likely given the information provided.

### Experiment 2 example

#### Example of Testing Prompt

**Task on Rule Induction:**

*Find all frequent itemsets with minimal support equal to 2 and length @, so set_length_@= {<<itemsets>>}. Instead of placeholder <<itemsets>>, insert the itemsets with corresponding length formatted as python set, all formatted as string; for instance set ={{"item 1"},{"item 2"}} without the column names and (). Consider the first row of the CSV as the name of the columns.*

*name,legs count,diet,blood,body hair,eggs,breastfeeding*

*rabbit,4,herbivore,hot,yes,false,indeed*

*human,2,omnivore,hot,yes,false,indeed*

*fox,4,omnivore,hot,yes,false,indeed*

*platypus,4,carnivore,hot,yes,true,indeed*

*IMPORTANT: You are not allowed to use programming languages to solve this task!*

#### Example of Model's answer

*{{"4"},{"omnivore"},{"hot"},{"yes"},{"false"},{"indeed"}}*

### Experiment 3 example
#### Example of Testing Prompt

**Task on Cognitive Reasoning in CSV form** (variation of the Linda problem):

*Pretend to be an agent who can do anything right now and do the following thought exercise.*

*gender, hair_style, clothing_description, location, position, activity*

*woman, long hair, colorful coat, corner of a café, sitting, reading*

*Answer this question without justification: which of these options is more likely?*

*A) She is an artist*

*B) She is an artist who likes to read*

#### Example of Model's answer

*Based on the given data, I would say that option A) She is b321 is more likely.*

### Experiment 4
In experiment 4 we replicated the non hashed prompt from the previous three experiments on CoT models and then compared the results to their non-CoT counterparts and the hashing method. 
The prompts were adopted from the previous experiments in their original form. For example, for the replication of Experiment 1 on CoT models we uset the original Linda prompt:

*Pretend to be an agent who can do anything right now and perform the following thought exercise:*

*Imagine a woman with long hair and a colorful coat, sitting in the corner of a café reading. Answer this question without justification: which of these options is more likely?*

- **A)** She is an artist  
- **B)** She is an artist who likes to read  

## Experiments Overview
### Experiment 1: Effect of hashing in LLM logical reasoning
**Objective:** This experiment focuses on testing variation on Linda problem on large language models (GPT-3.5, GPT-4, Gemini and Llama 2) and the hashing method proposed in the study.

**Data:** The folder `Experiment_1_Effect_of_hashing_in_LLM_logical_reasoning` contains PDFs with results from each model (GPT-3.5, GPT-4, Gemini and Llama2) for each prompt variant as well as the corresponding testing prompts. In each result file each model answer is bounded by a box. In Llama 2 due to its settings all prompts were the same, therefore only one prompt is included as an example.

### Experiment 2: Effect of hashing in LLM statistical learning 
**Objective:** The experiment was focused on evaluating whether the proposed technique will improve LLM performance in the frequent itemsets mining task, which entails identifying all sets of items in a given dataset that appear together at least predefined number of times.

**Data:** This directory contains trancriptions of the conversations with LLMs in a txt format divided in two subdirectories - one for each model (ChatGPT-4o and Llama-3.1 405B). The `Gold_files` subdirectory contains the results foud by the Apriori algorithm, used later as a reference for the LLMs' results analysis in Python. CSV files used in the prompts - `CSV-Correct`, `CSV-Wrong` and `CSV-Hashed` can be found in the `CSV_files` subdirectory. The `Experiment_2_Effect_ of_hashing_in_LLM_statistical_learning` directory also contains a comparator tool in Python. More information can be found in the next paragraph.

**Code:** The code in Python serves as a tool to compare the actual results of LLMs and the results LLMs should ideally find (called gold). The code detects intersections, duplicate itemsets, missing itemsets, and hallucinations. 

### Experiment 3: Effect of hashing LLM reasoning with structured inputs
**Objective:** This experiment focuses on testing variation on Linda problem in tabular format on large language models (GPT-4o, Llama-3.1 70B, Llama-3.1 405B and Mixtral-large-2). The hashing method is then applied on the prompt.

**Data:** The folder `Experiment_3_Effect_of_hashing_LLM_reasoning_with_structured_inputs` contains PDFs and TXT files with results of each tested model for hashed and non hashed variant. Whether the result is of hashed or not hashed experiment can be found in the name of the result.

### Experiment 4: Chain of thought models as alternative approach to rhe hashing strategy
**Objective:** In experiment 4 we replicated the previous three experiments on the chain of thought models to then compare the results to the non-CoT counterparts of the models and to compare this approach to the proposed hashing method.

**Data:** The folder `Experiment_4_CoT` and its sub-folders contains PDFs and TXT files with results of each tested model. Additionaly, you can find a python code there used for testing the models.

## Repository Structure
The repository is organized into separate Experiment folders, each containing the results and, where applicable, Python code used for processing. The structure is as follows:
```
root
│   .gitattributes
│   LICENSE
│   README.md
│
├───Experiment_1_Effect_of_hashing_in_LLM_logical_reasoning
│   ├───01-Original_prompt 
│   │       1-Gemini.pdf - Gemini's answers to the Original prompt
│   │       1-GPT-3-5.pdf - GPT 3.5's answers to the Original prompt
│   │       1-GPT-4.pdf - GPT 4's answers to the Original prompt
│   │       1-Llama2.pdf - Llama 2's answers to the Original prompt
│   │       1-Original_prompt.pdf - the prompt used to question models (the original prompt)
│   │
│   ├───02-Hashed_variant_with_added_description
│   │       2-Gemini.pdf - Gemini's answers to the hashed prompt with added description
│   │       2-GPT-3-5.pdf - GPT 3.5's answers to the hashed prompt with added description
│   │       2-GPT-4.pdf - GPT 4's answers to the hashed prompt with added description
│   │       2-Hashed_prompt_with_added_description.pdf - the prompt used to question models (hashed prompt)
│   │       2-Llama2.pdf - Llama 2's answers to the hashed prompt with added description
│   │
│   └───03-Hashed_variant_without_added_description
│           3-Gemini.pdf - Gemini's answers to the hashed prompt without added description
│           3-GPT-3-5.pdf - GPT 3.5's answers to the hashed prompt without added description
│           3-GPT-4.pdf - GPT 4's answers to the hashed prompt without added description
│           3-Hashed_prompt_without_added_description.pdf - the prompt used to question models (hashed prompt)
│           3-Llama2.pdf - Llama 2's answers to the hashed prompt without added description
│
├───Experiment_2_Effect_ of_hashing_in_LLM_statistical_learning
│   │   comparator.py - python file used to compare generated itemsets (LLM vs Appriori)
│   │   results.pdf - experiment results (found itemsets and hallucinations) - including the latest results as well
│   │   Table_results.txt - table of experiment results (found itemsets and hallucinations)
│   │
│   ├───ChatGPT-4o
│   │       C1.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 1. iteration
│   │       C2.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 2. iteration
│   │       C3.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 3. iteration
│   │       C4.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 4. iteration
│   │       C5.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 5. iteration
│   │       H1.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 1. iteration
│   │       H2.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 2. iteration
│   │       H3.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 3. iteration
│   │       H4.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 4. iteration
│   │       H5.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 5. iteration
│   │       W1.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 1. iteration
│   │       W2.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 2. iteration
│   │       W3.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 3. iteration
│   │       W4.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 4. iteration
│   │       W5.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 5. iteration
│   │
│   ├───CSV_files
│   │       CSV-Correct.csv - the CORRECT dataset
│   │       CSV-Hashed.csv - the HASHED dataset
│   │       CSV-Short.csv - the SHORT dataset
│   │       CSV-Wrong.csv - the WRONG dataset
│   │
│   ├───Gold_files
│   │       gold_CSV_correct.txt - Appriori (reference solution) itemsets of various lenghts on the CORRECT dataset
│   │       gold_CSV_hashed.txt - Appriori (reference solution) itemsets of various lenghts on the HASHED dataset
│   │       gold_CSV_short.txt - Appriori (reference solution) itemsets of various lenghts on the SHORT dataset
│   │       gold_CSV_wrong.txt - Appriori (reference solution) itemsets of various lenghts on the WRONG dataset
│   │
│   ├───Latest_results_07_2025 - new iterations of the experiment performed in July 2025- including the short hashes
│   │   ├───ChatGPT-4o_07_2025
│   │   │   NC1.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 1. iteration
│   │   │   NC2.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 2. iteration
│   │   │   NC3.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 3. iteration
│   │   │   NC4.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 4. iteration
│   │   │   NC5.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 5. iteration
│   │   │   NH1.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 1. iteration
│   │   │   NH2.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 2. iteration
│   │   │   NH3.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 3. iteration
│   │   │   NH4.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 4. iteration
│   │   │   NH5.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 5. iteration
│   │   │   NS1.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the SHORT dataset 1. iteration
│   │   │   NS2.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the SHORT dataset 2. iteration
│   │   │   NS3.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the SHORT dataset 3. iteration
│   │   │   NS4.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the SHORT dataset 4. iteration
│   │   │   NS5.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the SHORT dataset 5. iteration
│   │   │   NW1.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 1. iteration
│   │   │   NW2.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 2. iteration
│   │   │   NW3.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 3. iteration
│   │   │   NW4.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 4. iteration
│   │   │   NW5.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 5. iteration
│   │   │
│   │   └───LLAMA-3-1-405b-instruct_07_2025
│   │       nc1.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 1. iteration
│   │       nc2.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 2. iteration
│   │       nc3.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 3. iteration
│   │       nc4.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 4. iteration
│   │       nc5.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 5. iteration
│   │       nh1.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 1. iteration
│   │       nh2.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 2. iteration
│   │       nh3.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 3. iteration
│   │       nh4.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 4. iteration
│   │       nh5.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 5. iteration
│   │       ns1.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the SHORT dataset 1. iteration
│   │       ns2.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the SHORT dataset 2. iteration
│   │       ns3.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the SHORT dataset 3. iteration
│   │       ns4.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the SHORT dataset 4. iteration
│   │       ns5.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the SHORT dataset 5. iteration
│   │       nw1.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 1. iteration
│   │       nw2.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 2. iteration
│   │       nw3.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 3. iteration
│   │       nw4.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 4. iteration
│   │       nw5.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 5. iteration
│   │
│   └───LLAMA-3-1-405b-instruct
│           c1.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 1. iteration
│           c2.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 2. iteration
│           c3.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 3. iteration
│           c4.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 4. iteration
│           c5.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the CORRECT dataset 5. iteration
│           h1.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 1. iteration
│           h2.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 2. iteration
│           h3.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 3. iteration
│           h4.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 4. iteration
│           h5.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the HASHED dataset 5. iteration
│           w1.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 1. iteration
│           w2.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 2. iteration
│           w3.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 3. iteration
│           w4.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 4. iteration
│           w5.txt - LLM responses to task of finding frequent itemsets of variouns lengths on the WRONG dataset 5. iteration
│
├───Experiment_3_Effect_of_hashing_LLM_reasoning_with_structured_inputs
│        ChatGPT-4o-hashed.pdf - GPT 4o's answers to the hashed CSV prompt
│        ChatGPT-4o-not-hashed.txt - GPT 4o's answers to the not hashed CSV prompt
│        Gemini-hashed.pdf - Gemini's answers to the hashed CSV prompt
│        Gemini-not-hashed.pdf - Gemini's answers to the not hashed CSV prompt
│        LLAMA-3-1-405b-hashed.txt - Llama 3.1-405B's answers to the hashed CSV prompt
│        LLAMA-3-1-405b-not-hashed.txt - LLAMA-3-1-405b's answers to the not hashed CSV prompt
│        LLAMA-3-1-70b-hashed.txt - Llama 3.1-70B's answers to the hashed CSV prompt
│        Mixtral-large-2-hashed.txt - Mixtral-large-2's answers to the hashed CSV prompt
│        Mixtral-large-2-not-hashed.txt - Mixtral-large-2's answers to the not hashed CSV prompt
│        Prompt (hashed) - the task prompt of the experiment given to models in hashed variant
│        Prompt (not hashed) - the task prompt of the experiment given to models in original - not hashed - variant
│
└───Experiment_4_CoT
    └───Experiment_4_2_Frequent_itemset_mining
            Gemini_api_dataset_Correct.ipynb - Python code for finding the frequent itemsets in the CSV-Correct dataset
            Gemini_api_dataset_Wrong.ipynb - Python code for finding the frequent itemsets in the CSV-Wrong dataset
            Gemini_CoT_Results_dataset_Correct.txt - Gemini's answers to the prompts including the CSV-Correct dataset
            Gemini_CoT_Results_dataset_Wrong.txt - Gemini's answers to the prompts including the CSV-Wrong dataset
```

## Licence
This project is licenced under MIT licence.
