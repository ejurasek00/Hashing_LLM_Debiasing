# Meaningless is better: hashing bias-inducing words in LLM prompts improves performance in logical reasoning and statistical learning.
### Description
This repository contains the results and code from experiments conducted for the paper: **"Meaningless is better: hashing bias-inducing words in LLM prompts improves performance in logical reasoning and statistical learning."**
The repository is organized into multiple experiments, each containing results (in PDF or text format), and, where applicable, Python code used to process and compare the results.
## Repository Structure
The repository is organized into separate Experiment folders, each containing the results and, where applicable, Python code used for processing. The structure is as follows:
```
root
│   .gitattributes
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
< POPIS STRUKTURY >
## Experiments Overview
### Experiment 1: Effect of hashing in LLM logical reasoning
**Objective:** This experiment focuses on testing variation on Linda problem on large language models (GPT-3.5, GPT-4, Gemini and Llama 2) and the hashing method proposed in the study.

**Data:** The folder contains PDFs with results from each model (GPT-3.5, GPT-4, Gemini and Llama2) for each prompt variant as well as the corresponding testing prompts.

### Experiment 2: Effect of hashing in LLM statistical learning 
**Objective:** 

**Data:** 

**Code:**

### Experiment 3: Effect of hashing LLM reasoning with structured inputs
**Objective:** 

**Data:**

## Important Note
This repository is read-only and meant solely for observation. No code, scripts, or executable files are provided, and no modifications to the data or results should be made.
## Licence
< Jaká licence? >
