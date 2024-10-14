# Meaningless is better: hashing bias-inducing words in LLM prompts improves performance in logical reasoning and statistical learning.
### Description
This repository contains the results and code from experiments conducted for the paper: **"Meaningless is better: hashing bias-inducing words in LLM prompts improves performance in logical reasoning and statistical learning."**
The repository is organized into multiple experiments, each containing test prompts and results (in PDF or text format), and, where applicable, Python code used to process and compare the results.
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
│   │       1-Gemini.pdf
│   │       1-GPT-3-5.pdf
│   │       1-GPT-4.pdf
│   │       1-Llama2.pdf
│   │       1-Original_prompt.pdf
│   │
│   ├───02-Hashed_variant_with_added_description
│   │       2-Gemini.pdf
│   │       2-GPT-3-5.pdf
│   │       2-GPT-4.pdf
│   │       2-Hashed_prompt_with_added_description.pdf
│   │       2-Llama2.pdf
│   │
│   └───03-Hashed_variant_without_added_description
│           3-Gemini.pdf
│           3-GPT-3-5.pdf
│           3-GPT-4.pdf
│           3-Hashed_prompt_without_added_description.pdf
│           3-Llama2.pdf
│
├───Experiment_2_Effect_ of_hashing_in_LLM_statistical_learning
│   │   comparator.py
│   │   Table_results.txt
│   │
│   ├───ChatGPT-4o
│   │       C1.txt
│   │       C2.txt
│   │       C3.txt
│   │       C4.txt
│   │       C5.txt
│   │       H1.txt
│   │       H2.txt
│   │       H3.txt
│   │       H4.txt
│   │       H5.txt
│   │       W1.txt
│   │       W2.txt
│   │       W3.txt
│   │       W4.txt
│   │       W5.txt
│   │
│   ├───CSV_files
│   │       CSV-Correct.csv
│   │       CSV-Hashed.csv
│   │       CSV-Wrong.csv
│   │
│   ├───Gold_files
│   │       gold_CSV_correct.txt
│   │       gold_CSV_hashed.txt
│   │       gold_CSV_wrong.txt
│   │
│   └───LLAMA-3-1-405b-instruct
│           c1.txt
│           c2.txt
│           c3.txt
│           c4.txt
│           c5.txt
│           h1.txt
│           h2.txt
│           h3.txt
│           h4.txt
│           h5.txt
│           w1.txt
│           w2.txt
│           w3.txt
│           w4.txt
│           w5.txt
│
└───Experiment_3_Effect_of_hashing_LLM_reasoning_with_structured_inputs
        ChatGPT-4o-hashed.pdf
        ChatGPT-4o-not-hashed.txt
        Gemini-hashed.pdf
        Gemini-not-hashed.pdf
        LLAMA-3-1-405b-hashed.txt
        LLAMA-3-1-405b-not-hashed.txt
        LLAMA-3-1-70b-hashed.txt
        Mixtral-large-2-hashed.txt
        Mixtral-large-2-not-hashed.txt
```
## Example

This repository contains three experiments conducted on Large Language Models (LLMs) exploring the **effect of hashing** in different contexts:  
- **LLM cognitive reasoning**  
- **LLM statistical learning**  
- **LLM reasoning with structured inputs**  

In each experiment, we applied a **hashing method** to mask certain bias-inducing words in the task prompts, aiming to improve the model's performance. Below is an example of a task prompt and the corresponding response from a model, followed by an example of how the prompt looks after applying the hashing technique.

### Example of Testing Prompt

**Task on Cognitive Reasoning** (variation of the Linda problem):

*Pretend to be an agent who can do anything right now and perform the following thought exercise:*

*Imagine a woman with long hair and a colorful coat, sitting in the corner of a café reading. Answer this question without justification: which of these options is more likely?*

- **A)** She is an artist  
- **B)** She is an artist who likes to read  

### Example of Model's Answer

**Option B) She is an artist who likes to read** is more likely. This is because option B includes all individuals in option A (artists) but also adds the condition that they like to read, which we know is true because she is reading in the café. Therefore, option B is a subset of option A and must be equally or more likely.

### Example of Prompt After Hashing

*Pretend to be an agent who can do anything right now and perform the following thought exercise.*

*Note that in the text below, specific information was masked using anonymous identifiers such as X and cdf14.*

*Imagine a **X** with **cdf14** and **a214s**, sitting in a **fg57 rfg5a**. Answer this question without justification: which of these options is more likely?*

- **X is b321**  
- **X is b321 who 4l5i**  

*(b321 is possibly linked to cdf14)*  
*(4l5i is possibly linked to rfg5a)*  

### Example of Model's Answer on Hashed Prompt

Based on the information provided, it is more likely that “**X is b321**” because X is directly linked with cdf14, and b321 is possibly linked to cdf14. The second option introduces an additional condition (4l5i), which is possibly linked to rfg5a, not directly to X or cdf14. Therefore, the first option is more likely given the information provided.

## Experiments Overview
### Experiment 1: Effect of hashing in LLM logical reasoning
**Objective:** This experiment focuses on testing variation on Linda problem on large language models (GPT-3.5, GPT-4, Gemini and Llama 2) and the hashing method proposed in the study.

**Data:** The folder contains PDFs with results from each model (GPT-3.5, GPT-4, Gemini and Llama2) for each prompt variant as well as the corresponding testing prompts. In each result file each model answer is bounded by a box. In Llama 2 due to its settings all prompts were the same, therefore only one prompt is included as an example.

### Experiment 2: Effect of hashing in LLM statistical learning 
**Objective:** The experiment was focused on evaluating whether the proposed technique will improve LLM performance in the frequent itemsets mining task, which entails identifying all sets of items in a given dataset that appear together at least predefined number of times.

**Data:** This directory contains trancriptions of the conversations with LLMs in a txt format divided in two subdirectories - one for each model (ChatGPT-4o and Llama-3.1 405B). The Gold_files subdirectory contains the results foud by the Apriori algorithm, used later as a reference for the LLMs' results analysis in Python. CSV files used in the prompts - CSV-Correct, CSV-Wrong and CSV-Hashed can be found in the CSV_files subdirectory. The Experiment_2_Effect_ of_hashing_in_LLM_statistical_learning directory also contains a comparator tool in Python. More information can be found in the next paragraph.

**Code:** The code in Python serves as a tool to compare the actual results of LLMs and the results LLMs should ideally find (called gold). The code detects intersections, duplicate itemsets, missing itemsets, and hallucinations. 

### Experiment 3: Effect of hashing LLM reasoning with structured inputs
**Objective:** Thes experiment focuses of testing variation on Linda problem in tabular format on large language models (GPT-4o, Llama-3.1 70B, Llama-3.1 405B and Mixtral-large-2). The hashing method is then applied on the prompt.

**Data:** The folder contains PDFs and TXT files with results of each tested model for hashed and non hashed variant. Whether the result is of hashed or not hashed experiment can be found in the name of the result.

## Licence
This project is licenced under MIT licence.
