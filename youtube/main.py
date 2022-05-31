import string
import stopwordsiso as stopwords
from collections import Counter
import spacy


text = open("Bella.txt", encoding="utf-8").read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

tokenized_words = cleaned_text.split()


stop_words = list(stopwords.stopwords("en"))

final_words = [word for word in tokenized_words if word not in stop_words and not word.isnumeric()]


with open('emotions.txt', 'r') as file:
    emotion_list = []
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

w = Counter(final_words)
print(w)
print(final_words)
print(emotion_list)


import spacy
def test_lemmatizer_initialize():
    nlp = spacy.load("en_core_web_sm")
    return_list = []
    for word in w:
        doc = nlp(word)
        for token in doc:
            return_list.append(token)
    print(return_list)

# fasfasfda

# test_lemmatizer_initialize()