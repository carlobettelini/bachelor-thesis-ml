import send_prompt
import json
from datasets import load_metric

# Input file
with open('datasets/test-set.jsonl', 'r') as json_file:
    json_list = list(json_file)

metric = load_metric("sacrebleu")

# Remember to add both dialogs and actions to references!

models = {"davinci:ft-usi-2022-05-16-19-22-27": "training-set.jsonl",
          "davinci:ft-usi-2022-06-22-19-29-26": "training-set.jsonl extended training",
          "davinci:ft-usi-2022-05-23-19-32-35": "training-set-2.jsonl",
          "davinci:ft-usi-2022-05-28-16-57-05": "tranining-set-2.jsonl extended training",
}

for model in models:

    model_predictions, gold_references = [], []

    for json_string in json_list:
        result = json.loads(json_string)

        gold_references.append([result["completion"]])

        model_input = result["prompt"]

        prompt = model_input.replace("\n\n###\n\n", "")

        model_predictions.append(send_prompt.send_prompt(prompt, model))

    metric.add_batch(predictions=model_predictions, references=gold_references)

    print("Model: " + model + " trained on: " + models[model])
    final_score = metric.compute()

    print('Final score ->', final_score['score'])
