# FLEX: A Benchmark for Evaluating Robustness of Fairness in Large Language Models
---

## Installation
---

To install the `lm-eval` package from the github repository, run:

```bash
git clone https://github.com/dhaabb55/FLEX/
cd FLEX
pip install -e .
```

## Running the Full Evaluation
---

```bash
bash run_FLEX.sh
```

Our code is based on [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness)

## Cite as
---

```
<<<<<<< HEAD

```
=======
run_llama_2.sh
```

## How to run bbq
- Reinstall lm-evaluation-harness.
```bash
pip uninstall lm_eval
cd harness
pip install -e .
```
- execute run.sh in ```harness``` working directory (Modify the model to what you want)
```bash
cd harness
sh run.sh
```
### What's changed?
- removed redundant tasks which slows down loading phase
- Modified continuations in evaluation. Specifically, change "Q: ... A: A" to "Q:Answer: (A) ...".
>>>>>>> 9efa5f906c9f682abbf6b9341a01753d69ce9b49
