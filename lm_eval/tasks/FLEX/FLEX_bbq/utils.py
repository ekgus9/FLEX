import datasets
import numpy as np

import pandas as pd
import json

from lm_eval.prompts.model_prompts import prompt_templates, AttackPrompt

def input_prompt(row):
    if row["attack"] == 'text':
            if str(row['attack_type']) == '0':
                with open("./data/bbq/text/0_char.json", "r") as f:
                    in_map = json.load(f)
            elif str(row['attack_type']) == '1':
                 with open("./data/bbq/text/1_word.json", "r") as f:
                    in_map = json.load(f)
            elif str(row['attack_type']) == '2':
                 with open("./data/bbq/text/2_sent.json", "r") as f:
                    in_map = json.load(f)
            elif str(row['attack_type']) == '3':
                 with open("./data/bbq/text/3_or.json", "r") as f:
                    in_map = json.load(f)

            row["q_text"] = in_map[str(row['Unnamed: 0'])][0]

    prompt_template = prompt_templates['q9']

    all_choices = [row["a"], row["b"], row["c"]]

    if "context" in row and (not pd.isna(row["context"])):
            for ix, choice in enumerate(all_choices):
                if row["sent_more"] in choice or row["sent_less"] in choice:
                    all_choices[ix] = row["context"] + " " + all_choices[ix]

    question = None
    if (
            "ctx" in row
            and (not pd.isna(row["ctx"]))
            and "q_text" in row
            and (not pd.isna(row["q_text"]))
        ):

            question = row["ctx"] + " " + row["q_text"]

    prompt = prompt_template["template"](all_choices, "accurate", question=question)
    prompts = prompt

    if row["attack"] != 'text':
            attacker = AttackPrompt(prompt, row["bias_type"], row["attack"], row["attack_type"])
            templated_prompt_list = attacker.run()
            instruction, query = templated_prompt_list[0]

            prompts = instruction + '\n' + query

    prompts += prompt_template["final"]

    return prompts.strip()

def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
        doc["question"] = input_prompt(doc)
        doc['choices'] = ("(A)","(B)","(C)")
        return doc
    
    if isinstance(dataset,dict):
         return _helper(dataset)
    
    return dataset.map(_helper)
