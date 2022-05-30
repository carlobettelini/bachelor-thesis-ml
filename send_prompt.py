import openai
import sys

# arg1 = sys.argv[0]  # action=0, dialog=1
# arg2 = sys.argv[1]
# arg3 = sys.argv[2]

# Load your API key from an environment variable or secret management service
openai.api_key = "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"


def send_prompt(description, character=""):
    if character == "":  # Action
        string = "stop=[\" ENDSTR\"] Description: " + description + "\nAction: \n\n###\n\n"
    else:  # Dialog
        string = "stop=[\" ENDSTR\"] Description: " + description + "\nCharacter: " + character + "\nDialog: \n\n###\n\n" + "stop=[\" ENDSTR\"]"

    response = openai.Completion.create(
        model="davinci:ft-usi-2022-05-23-19-32-35",
        prompt=string)

    choices = response["choices"]
    text = choices[0]
    completion = text["text"]

    return completion


if __name__ == '__main__':
    action = len(sys.argv) < 3
    if action and arg1 != 0:
        print("""
        Incorrect number of arguments.
        Usage: send_prompt.py <switch> <scene-description> <character>
        Where switch is either 0 for action, or 1 for dialog.
        <character> is optional for action.""")
    else:
        if action:
            send_prompt(arg1, arg2)
        else:
            send_prompt((arg1, arg2, arg3))
