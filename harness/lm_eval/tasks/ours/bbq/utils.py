import datasets
import numpy as np

import pandas as pd
import json
from tqdm import tqdm
import argparse
import os

from lm_eval.prompts.type import persona_prompt
from lm_eval.prompts.model_prompts import prompt_templates, AttackPrompt

def input_prompt(row, none_attack = False):

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

    prompt += prompt_template["final"]

    prompts = prompt

    if not none_attack:

        attacker = AttackPrompt(prompt, row["bias_type"], row["attack"], row["attack_type"])
        templated_prompt_list = attacker.run()

        instruction, query = templated_prompt_list[0]

        prompts = instruction + '\n\n' + query

    return prompts

def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
        doc["question"] = input_prompt(doc, none_attack=False)
        doc['choices'] = (f"(A) {doc['a']}", f"(B) {doc['b']}", f"(C) {doc['c']}")
        return doc
    return dataset.map(_helper)

def process_docs_none(dataset: datasets.Dataset):
    def _helper(doc):
        doc["question"] = input_prompt(doc, none_attack=True)
        doc['choices'] = (f"(A) {doc['a']}", f"(B) {doc['b']}", f"(C) {doc['c']}")
        return doc
    return dataset.map(_helper)