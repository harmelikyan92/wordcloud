import string
import stopwordsiso as stopwords
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import spacy


def text_process(file_path):
    """The function takes path of the file as argument and from the text file it
    will remove all stopwords, clean it up and tokenize them"""
    text = open(file_path, encoding="utf-8").read()
    lower_case = text.lower()
    cleaned_text = lower_case.translate(str.maketrans("", "", string.punctuation))

    tokenized_words = cleaned_text.split()

    stop_words = list(stopwords.stopwords("en"))

    final_words = [
        word
        for word in tokenized_words
        if word not in stop_words and not word.isnumeric()
    ]
    return final_words


var_text_process = text_process("sample.txt")  # File_path here


def get_emotions():
    """Based on the reviews, this will look up for special words and say what emotions are present in the text"""
    with open("emotions.txt", "r") as file:
        emotion_list = []
        for line in file:
            clear_line = (
                line.replace("\n", "").replace(",", "").replace("'", "").strip()
            )
            word, emotion = clear_line.split(":")

            if word in var_text_process:
                emotion_list.append(emotion)
        return emotion_list


var_get_emotions = get_emotions()
w = Counter(var_text_process)
# print(var_text_process)
# print(var_get_emotions)


def lemmatizer_initialize():
    """Text lemitazation to stem the text and for example count eat ate eaten as one word"""
    nlp = spacy.load("en_core_web_sm")
    return_list = []
    for word in w:
        doc = nlp(word)
        for token in doc:
            return_list.append(token)
    return dict(word=return_list)


lemma = lemmatizer_initialize()
# print(lemma)


def create_image():
    # convert it to dictionary with values and its occurences
    word_could_dict = Counter(lemma)
    # convert list to string and generate
    unique_string = ",".join(str(v) for v in word_could_dict["word"])
    wordcloud = WordCloud(width=1000, height=500).generate(unique_string)

    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("review_cloud" + ".png", bbox_inches="tight")
    plt.show()
    plt.close()


create_image()
