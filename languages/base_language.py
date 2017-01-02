import nltk
import random
import re

"""
BaseLanguage class

Defines shared functionality among all languages

To define your own language, you should override:

get_stripped_pos (return an array of POS to strip from the sentence)
get_encoding_dict (an array of tuples of character combinations and their replacements)
get_case_sensitive_encoding (returns true if encoding is case sensitive)
parse_syntax (should return an array of words)

nltk packages: punkt, averaged_perceptron_tagger
"""
class BaseLanguage:
    """
    Fluency = chance a word is left as the original, from 0.0-1.0
    """
    def __init__(self, fluency=0.0):
        self.fluency = fluency
        print("Fluency set to " + str(fluency))

    def get_stripped_pos(self):
        # Could do something like ["DT", "PRP"], etc. Based on NLTK tags
        return []

    """
    Returns an array of tuples with (character pattern, replacement) to encode words
    Searches in order, so you can do stuff like:
    [
        ("ou", "yu"),
        ("u", "s")
    ]
    """
    def get_encoding_dict(self):
        return []

    def get_case_sensitive_encoding(self):
        return False

    """
    Translation follows the following steps
    - Tokenize Sentence
    - Tag parts of speech
    - Strip any unused parts of speech as defined by the language
    - Encode english
    - Parse syntax
    - Render sentence
    """
    def translate(self, sentence):
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        stripped = self.strip(tagged)
        encoded = self.encode(stripped)
        sentence = self.parse_syntax(encoded)

        return sentence

    """
    Strips parts of speech from the set of tokens
    """
    def strip(self, tagged_pos):
        tagged_copy = list(tagged_pos) # Store a copy
        stripped_pos = self.get_stripped_pos()

        for tagged in tagged_pos:
            if tagged[1] in stripped_pos:
                tagged_copy.remove(tagged)

        return tagged_copy

    """
    Encodes each word in the set of tokens
    """
    def encode(self, tagged_pos):
        rules = self.get_encoding_dict()
        case_sensitive = self.get_case_sensitive_encoding()
        encoded = []
        common_regex = "(?![^{]*})" # A negative lookahead

        for word in tagged_pos:
            if(random.random() < self.fluency):
                continue
            word_temp = word[0]
            for rule in rules:
                pattern = rule[0] + common_regex
                word_temp = re.sub(pattern, "{" + rule[1] + "}", word_temp)

            # This will strip out any {} in the word, which we use to prevent duplicate encoding
            encoded.append((word_temp.translate(None, "{").translate(None, "}"), word[1]))

        return encoded

    """
    If not overridden, just returns a join of the words in the tagged_pos
    """
    def parse_syntax(self, tagged_pos):
        return " ".join([word[0] for word in tagged_pos])
