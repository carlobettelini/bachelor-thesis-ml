import json

# Input file
with open('../SummScreen/ForeverDreaming/fd_train.json', 'r') as json_file:
    json_list = list(json_file)

# Output file
outfile = open('../datasets/new-training-set.jsonl', 'w')

for json_str in json_list:
    result = json.loads(json_str)
    prompt = (' '.join(map(str, result['Recap']))).replace('"', " '").replace(" '", "\'")
    completion = (r'\n'.join(map(str, result['Transcript']))).replace('"', " '").replace(" '", "\'")
    disallowed_characters = ["@@ ", "(", ")", "\\"]
    for chara in disallowed_characters:
        prompt = prompt.replace(chara, "")
        completion = completion.replace(chara, "")
    entry = '{"prompt":"' + prompt + r'\n\n###\n\n","completion":" ' + completion + ' ENDSTR"}'
    # using map() + split()
    # Tokenizing strings in list of strings
    res = list(map(str.split, test_list))
    # Append line at the end of file
    outfile.write(entry)
    outfile.write('\n')

# Write to jsonl file.
outfile.close()
