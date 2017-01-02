import nltk
from nltk.data import load

sentence = "this is a test sentence"
sentence2 = "she gave him the ball"

for sen in [sentence, sentence2]:
    tokens = nltk.word_tokenize(sen)
    tagged = nltk.pos_tag(tokens)
    print(tagged)
