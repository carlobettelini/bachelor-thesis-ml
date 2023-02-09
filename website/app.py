import math

from flask import Flask, jsonify, render_template, request
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "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"

models = {"D1": "davinci:ft-usi-2022-05-16-19-22-27",
          "D1+": "davinci:ft-usi-2022-06-22-19-29-26",
          "D2": "davinci:ft-usi-2022-05-23-19-32-35",
          "D2+": "davinci:ft-usi-2022-05-28-16-57-05"
          }

app = Flask(__name__)


@app.route("/")
def app_base():
    return render_template("base.html")


@app.route("/write_screenplay", methods=["POST"])
def write_screenplay():
    # Read the input from url arguments
    description = request.args.get("prompt")
    model = request.args.get("model").strip()

    print(description, model)

    prompt = description + ":\n\n###\n\n"

    # Create a completion
    response = openai.Completion.create(
        model=models[model],
        prompt=prompt,
        max_tokens=300,
        temperature=0.2,
        stop="ENDSTR"
    )

    choices = response["choices"]
    text = choices[0]
    completion = text["text"]

    # Format the completion in a readable way
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
            write_in_upper = False
            screenplay += "\n"
        else:
            word = item
            if write_in_upper:
                word = item.upper()
            screenplay += word + " "

    output = screenplay.strip()
    print(output)
    return jsonify({"screenplay": output.replace("\n", '<br>')})


# def app_solve():

#         # Build a solution matrix from the SAT model
#         for item in model:
#             key = str(item)
#             value = int(str(model[item])) + 1
#             solution[key] = value
#
#         print("Satisfiable", solution)
#         return jsonify({"sat": True, "model": solution})
#     else:
#         print("Unsatisfiable")
#         return jsonify({"sat": False})
