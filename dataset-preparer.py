# STRUCTURE OF A SCREENPLAY:

#       ACTION
#       ACTION

#      CHARACTER
#     TEXT-DIALOG

#       ACTION

#      CHARACTER
#     TEXT-DIALOG
#     TEXT-DIALOG

#   OTHER CHARACTER
#     TEXT-DIALOG


f = open('data_to_prepare.txt', 'r')

onGoing = False
prompt = True
totNumber = 0
lines = f.readlines()

mainStr = '{"prompt": "'

for idx, elem in enumerate(lines):
    thisElem = elem
    nextElem = lines[(idx + 1) % len(lines)]

    if thisElem == '\n':
        if nextElem == '\n':
            if prompt:
                totNumber += 1
                mainStr += r':\n\n###\n\n", "completion": "'
            else:
                mainStr += ' ENDSTR"}' + '\n' + '{"prompt": "'
            prompt = not prompt
        continue

    if prompt:
        mainStr += thisElem.strip()
    else:
        if onGoing:
            mainStr += thisElem.strip() + ' '
            if nextElem == '\n':
                onGoing = False
        else:
            if thisElem.isupper():
                if nextElem != '\n':
                    mainStr += 'CHARACTER: ' + thisElem.strip() + ' DIALOG: '
                    onGoing = True
            else:
                mainStr += 'ACTION: '
                mainStr += thisElem.strip() + ' '
                if nextElem != '\n':
                    onGoing = True

mainStr += ' ENDSTR"}'
print(mainStr)
print("Total: ", totNumber)
