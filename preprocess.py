from transformers import AutoTokenizer
import json

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

with open('./datasets/SummScreen/ForeverDreaming/fd_train.json', 'r') as json_file:
    json_list = list(json_file)

prompt_sentences = []
completion_sentences = []

for json_str in json_list:
    result = json.loads(json_str)
    prompt_sentences.append(result["Recap"])
    completion_sentences.append(result["Transcript"])
    print(prompt_sentences)
# batch_sentences = [
#     "But what about second breakfast?",
#     "Don't think he knows about second breakfast, Pip.",
#     "What about elevensies?",
# ]
# # Set the padding parameter to True to pad the shorter sequences in the batch to match the longest sequence
# # Set the truncation parameter to True to truncate a sequence to the maximum length accepted by the model
# encoded_input = tokenizer(batch_sentences, padding=True, truncation=True, return_tensors="tf")
# print(encoded_input)
# {'input_ids': <tf.Tensor: shape=(2, 9), dtype=int32, numpy=
# array([[101, 1252, 1184, 1164, 1248, 6462, 136, 102, 0, 0, 0, 0, 0, 0, 0],
#        [101, 1790, 112, 189, 1341, 1119, 3520, 1164, 1248, 6462, 117, 21902, 1643, 119, 102],
#        [101, 1327, 1164, 5450, 23434, 136, 102, 0, 0, 0, 0, 0, 0, 0, 0]],
#       dtype=int32)>,
#  'token_type_ids': <tf.Tensor: shape=(2, 9), dtype=int32, numpy=
# array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int32)>,
#  'attention_mask': <tf.Tensor: shape=(2, 9), dtype=int32, numpy=
# array([[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int32)>}