import nltk
from nltk.data import load
from languages.base_language import BaseLanguage

sentence = "this is a test sentence"
sentence2 = "she gave him the ball"

bl = BaseLanguage()

for sen in [sentence, sentence2]:
    print(bl.translate(sen))

def install_nltk_corpora():
    nltk.download("punkt")
    nltk.download("averaged_perceptron_tagger")
