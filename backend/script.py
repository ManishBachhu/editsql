import json
import sys
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
def read_json(file):
    f = open(file)
    data = json.load(f)
    f.close()
    return data
def edit_json(text):
    file_path = "dev_no_value.json"
    data = read_json(file_path)
    data[0]["final"]["utterance"] = text
    data[0]["interaction"][0]["utterance"] = text
    data[0]["interaction"][0]["utterance_toks"] = word_tokenize(text)
    return data
if __name__ == '__main__':
    text = "How is this?"
    print(edit_json(text))
    