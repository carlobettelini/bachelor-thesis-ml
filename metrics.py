import send_prompt
import json
from datasets import load_metric

# Input file
with open('./test-set.jsonl', 'r') as json_file:
    json_list = list(json_file)

metric = load_metric("sacrebleu")

model_predictions, gold_references = [], []

for json_string in json_list:
    result = json.loads(json_string)

    gold_references.append(result["completion"])

    model_input = result["prompt"]

    a, b = "Description: ", "\n"
    description, character = model_input[model_input.find(a) + len(a):model_input.find(b)], ""

    if model_input.find("Action:") == -1:
        a, b = "Character: ", "\nDialog: "
        character = model_input[model_input.find(a) + len(a):model_input.find(b)]

    model_predictions.append(send_prompt.send_prompt(description, character))

metric.add_batch(predictions=model_predictions, references=gold_references)

final_score = metric.compute()
print(final_score)
