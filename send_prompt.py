import openai
import sys

# Load your API key from an environment variable or secret management service
openai.api_key = "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"


models = {"davinci:ft-usi-2022-05-16-19-22-27": "training-set.jsonl",
          "davinci:ft-usi-2022-06-22-19-29-26": "training-set.jsonl extended training",
          "davinci:ft-usi-2022-05-23-19-32-35": "training-set-2.jsonl",
          "davinci:ft-usi-2022-05-28-16-57-05": "tranining-set-2.jsonl extended training",
}

prompts_1 = ["The victim receives a call from the murder, that ask them about their favorite horror movie",
             "The knight faces the dragon to save the princess",
             "The wizard turns his opponent into a frog",
             "Ian reaches the source of life",
             "Darth Vader attacks the Jedi"]

prompts_2 = ["The murder asks the victim about their favorite horror movie",
             "The knight faces the dragon",
             "The enemy turns into a frog",
             "Ian takes the source of life from the coffer",
             "Darth Vader attacks the Jedi"]


# def send_prompt():
#     for key in models:
#         model = key
#         model_description = models[model]
#
#         print("\n\nPrinting results using model " + model + " trained with " + model_description + "\n...\n")
#
#         for prompt in prompts_1:
#             prompt += prompt + ":\n\n###\n\n"
#
#             response = openai.Completion.create(
#                 model=model,
#                 prompt=prompt,
#                 max_tokens=300,
#                 temperature=0.5,
#                 stop="ENDSTR"
#             )
#
#             choices = response["choices"]
#             text = choices[0]
#             completion = text["text"]
#
#             print(completion)

def send_prompt(description):

    prompt = description + ":\n\n###\n\n"

    response = openai.Completion.create(
        model="davinci:ft-usi-2022-06-22-19-29-26",
        prompt=prompt,
        max_tokens=300,
        temperature=0.1,
        stop="ENDSTR"
    )

    choices = response["choices"]
    text = choices[0]
    completion = text["text"]

    list_of_strings = completion.split(" ")
    screenplay = ""
    write_in_upper = False

    for item in list_of_strings:
        if item == "ACTION:":
            screenplay += "\n\n"
        elif item == "CHARACTER:":
            screenplay += "\n\n"
            write_in_upper = True
        elif item == "DIALOG:":
            screenplay += "\n"
        else:
            word = item
            if write_in_upper:
                word = item.upper()
                write_in_upper = False
            screenplay += word + " "

    print(screenplay)


if __name__ == '__main__':
    while 1:
        user_input = input("Description of the scene:")
        send_prompt(user_input)


# def send_prompt(description, model):
#     result = description + "\n\n###\n\n"
#
#     response = openai.Completion.create(
#         max_tokens=200,
#         stop="ENDSTR",
#         model=model,
#         prompt=result,
#         temperature=0.5
#     )
#
#     choices = response["choices"]
#     text = choices[0]
#     completion = text["text"]
#
#     return completion
