import nltk
from nltk.data import load
from languages.base_language import BaseLanguage
from languages.fantasy.high_common import HighCommon

test_sentences = [
    "she gave him the ball",
    "testing a test sentence for testing",
    "Hello, traveller!",
    "Would you like to buy some goods?",
    "Attack!",
    "Farewell for now.",
    "I suppose... if that is what you want.",
    "Whew! I am a bit stressed now.",
    "I would rather not do that, Julian."
]

languages = [
    ("Base", BaseLanguage()),
    ("High Common", HighCommon()),
    ("High Common", HighCommon(fluency=0.5)),
    ("High Common", HighCommon(fluency=0.9)),
    ("High Common", HighCommon(fluency=1.0))
]

# Get max length test sentence for formatting
sen_width = 0
for sentence in test_sentences:
    sen_width = max(sen_width, len(sentence))
format_str = "{0:<" + str(sen_width) + "}  -->  {1:<" + str(sen_width) + "}"

for language in languages:
    print("\n\nUsing language: " + language[0] + " with " + str(language[1].fluency) + " fluency\n")
    print(format_str.format("English", language[0]))
    print("#######################################")
    for sentence in test_sentences:
        print(format_str.format(sentence, language[1].translate(sentence)))

def install_nltk_corpora():
    nltk.download("punkt")
    nltk.download("averaged_perceptron_tagger")
