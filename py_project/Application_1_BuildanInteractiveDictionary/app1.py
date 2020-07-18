import json

from difflib import get_close_matches

data = json.load(open("1.2 data.json"))

def translate(w):

    w = w.lower()

    if w in data:

        return data[w]

    elif len(get_close_matches(w, data.keys())) > 0:

        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])

        if yn == "Y":

            return data[get_close_matches(w, data.keys())[0]]

        elif yn == "N":

            return "This Word Dosen't Exist"

        else:

            return "we didn't understand your entry"

    else:

        return "This Word Dosen't Exist Please Double Check Your Word"

while True:
    
    word = input("Enter Your Word (or q to quit): ")
    if word == 'q':
        break
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)