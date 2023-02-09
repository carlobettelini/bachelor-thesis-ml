import json

separator = r"\n\n###\n\n"

# Input file
with open('../datasets/training-set.jsonl', 'r') as json_file:
    json_list = list(json_file)

# Output file
outfile = open('../datasets/training-set-2.jsonl', 'a')

for json_str in json_list:
    result = json.loads(json_str)

    # Prompt
    prompt = result['prompt']
    prompt = prompt[:-len(separator)+3]
    prompt = "Description: " + prompt

    completion = result['completion']

    # Searches whether there is an instance of a character, of an action first.
    character_index = completion.find("CHARACTER")
    action_index = completion.find("ACTION")

    if action_index < character_index and action_index != -1 or character_index == -1:
        action_index += len("Action: ")
        string = completion[action_index:]

        # This cuts the action in the instance a character starts talking, or another action takes place
        character_index = string.find("CHARACTER")
        action_index = string.find("ACTION")
        if character_index < action_index and character_index != -1 or action_index == -1:
            string = string[:character_index]
        else:
            string = string[:action_index]
        string = string.replace('ENDST', '').strip()

        # Builds the prompt given the previous data.
        prompt += r"\nAction: " + separator
        completion = " " + string

    else:
        dialog_index = completion.find("DIALOG")  # Dialog comes right after a character
        character_index += len("Character: ")  # To remove substring 'CHARACTER: '
        character = completion[character_index:dialog_index]  # Retrieves the name of the character

        dialog_index += len('DIALOG: ')  # To remove substring 'DIALOG: '
        string = completion[dialog_index:]  # Finds the dialog of the character

        # This cuts the dialog before an action begins, or another character starts talking.
        character_index = string.find("CHARACTER")
        action_index = string.find("ACTION")
        if character_index < action_index and character_index != -1 or action_index == -1:
            string = string[:character_index]
        else:
            string = string[:action_index]
        string = string.replace('ENDST', '').strip()

        # Builds the prompt given the previous data.
        prompt += r"\nCharacter: " + character.strip() + r"\nDialog:" + separator
        completion = " " + string

    line = r'{"prompt":"' + prompt + '","completion":"' + completion + ' ENDSTR"}'

    # Append line at the end of file
    outfile.write(line)
    outfile.write('\n')

# Write to jsonl file.
outfile.close()
