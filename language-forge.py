import nltk
import sys
from optparse import OptionParser
from nltk.data import load
from languages.base_language import BaseLanguage
from languages.fantasy.high_common import HighCommon

possible_languages = {
    "base": ("Base", BaseLanguage),
    "high_common": ("High Common", HighCommon)
}

parser = OptionParser("usage: %prog [options] sentence")
parser.add_option("-t", "--test", dest="test",
                  action="store_true", default=False)
parser.add_option("-l", "--language", dest="language", action="append", type="choice", choices=list(possible_languages.keys()),
                 help="Languages which to translate the given string. Options: " + ", ".join([s for s in possible_languages.keys()]), metavar="LANG", default=[])
parser.add_option("-f", "--fluency", dest="fluency", action="store", type="float",
                 help="Listener's fluency with the language", metavar="FLUENCY", default=0.0)
parser.add_option("-i", "--install-corpora", dest="install", action="store_true", default=False,
                 help="Install ntlk corpora")

(options, args) = parser.parse_args()

sentences = []
languages = []


if options.install:
    nltk.download("punkt")
    nltk.download("averaged_perceptron_tagger")
if options.test:
    sentences = sentences + [
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

    languages = languages + [
        ("Base", BaseLanguage()),
        ("High Common", HighCommon()),
        ("High Common", HighCommon(fluency=0.5)),
        ("High Common", HighCommon(fluency=0.9)),
        ("High Common", HighCommon(fluency=1.0))
    ]
else:
    # support piping in a file
    if not sys.stdin.isatty():
        input_stream = sys.stdin
    else:
        input_stream = args
    for line in input_stream:
        sentences.append(line.rstrip())

    for lang in options.language:
        languages.append((possible_languages[lang][0],
                          possible_languages[lang][1](fluency=options.fluency)))

# Get max length test sentence for formatting
sen_width = 0
for sentence in sentences:
    sen_width = max(sen_width, len(sentence))
format_str = "{0:<" + str(sen_width) + "}  -->  {1:<" + str(sen_width) + "}"

for language in languages:
    print("\n\nUsing language: " + language[0] + " with " + str(language[1].fluency) + " fluency\n")
    print(format_str.format("English", language[0]))
    print("#######################################")
    for sentence in sentences:
        print(format_str.format(sentence, language[1].translate(sentence)))
