import nltk
import random
import re

"""
BaseLanguage class

Defines shared functionality among all languages

To define your own language, you should override:

get_stripped_pos (return an array of POS to strip from the sentence)
get_encoding_rules (an array of tuples of character combinations and their replacements)
get_case_sensitive_encoding (returns true if encoding is case sensitive)
parse_syntax (should return an array of words)

nltk packages: punkt, averaged_perceptron_tagger
"""
class BaseLanguage(object):
    """
    Fluency = chance a word is left as the original, from 0.0-1.0
    """
    def __init__(self, fluency=0.0):
        self.fluency = fluency

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

    Also supports arrays in the first parameter, and operates on those in order by max length to lowest length

    You may want to use a list of graphemes to assist in your design. For your use, I've listed a started list of tuples below
    [
        (["b", "bb"], ""),
        (["d", "dd", "ed"], ""),
        (["f", "ff", "ph", "gh", "lf", "ft"], ""),
        (["g", "gg", "gh", "gu", "gue"], ""),
        (["h", "wh"], ""),
        (["j", "ge", "g", "dge", "di", "gg"], ""),
        (["k", "c", "ch", "cc", "lk", "qu", "q", "ck", "x"], ""),
        (["l", "ll"], ""),
        (["m", "mm", "mb", "mn", "lm"], ""),
        (["n", "nn", "kn", "gn", "pn"], ""),
        (["p", "pp"], ""),
        (["r", "rr", "wr", "rh"], ""),
        (["s", "ss", "c", "sc", "ps", "st", "ce", "se"], ""),
        (["t", "tt", "th", "ed"], ""),
        (["v", "f", "ph", "ve"], ""),
        (["w", "wh", "u", "o"], ""),
        (["y", "i", "j"], ""),
        (["z", "zz", "s", "ss", "x", "ze", "se"], ""),
        (["a", "ai", "au"], ""),
        (["a", "ai", "eigh", "aigh", "ay", "er", "et", "ei", "au", "ea", "ey"], ""),
        (["e", "ea", "u", "ie", "ai", "a", "eo", "ei", "ae", "ay"], ""),
        (["e", "ee", "ea", "y", "ey", "oe", "ie", "i", "ei", "eo", "ay"], ""),
        (["i", "e", "o", "u", "ui", "y", "ie"], ""),
        (["i", "y", "igh", "ie", "uy", "ye", "ai", "is", "eigh"], ""),
        (["o", "a", "ho", "au", "aw", "ough"], ""),
        (["o", "oa", "oe", "ow", "ough", "eau", "oo", "ew"], ""),
        (["o", "oo", "u", "ou"], ""),
        (["u", "o", "oo", "ou"], ""),
        (["o", "oo", "ew", "ue", "oe", "ough", "ui", "oew", "ou"], ""),
        (["u", "you", "ew", "iew", "yu", "ul", "eue", "eau", "ieu", "eu"], ""),
        (["oi", "oy", "uoy"], ""),
        (["ow", "ou", "ough"], ""),
        (["a", "er", "i", "ar", "our", "or", "e", "ur", "re", "eur"], ""),
        (["air", "are", "ear", "ere", "eir", "ayer"], ""),
        (["a", "ar", "au", "er", "ear"], ""),
        (["ir", "er", "ur", "ear", "or", "our", "yr"], ""),
        (["aw", "a", "or", "oor", "ore", "oar", "our", "augh", "ar", "ough", "au"], ""),
        (["ear", "eer", "ere", "ier"], ""),
        (["ure", "our"], ""),
        (["s", "si", "z"], ""),
        (["ch", "tch", "tu", "ti", "te"], ""),
        (["sh", "ce", "s", "ci", "si", "ch", "sci", "ti"], ""),
        (["th"], ""),
        (["ng", "n", "ngue"], ""),
    ]

    And here is one sorted by length with duplicates removed
    [
        (['ch', 'cc', 'lk', 'qu', 'ck', 'k', 'c', 'q', 'x'], ""),
        (['eigh', 'aigh', 'ay', 'er', 'et', 'ei', 'ea', 'ey'], ""),
        (['ss', 'sc', 'ps', 'st', 'ce', 'se', 's'], ""),
        (['you', 'iew', 'eue', 'ieu', 'yu', 'ul', 'eu'], ""),
        (['ff', 'ph', 'gh', 'lf', 'ft', 'f'], ""),
        (['our', 'eur', 'ar', 'or', 'ur', 're'], ""),
        (['ayer', 'air', 'are', 'ear', 'ere', 'eir'], ""),
        (['mm', 'mb', 'mn', 'lm', 'm'], ""),
        (['nn', 'kn', 'gn', 'pn', 'n'], ""),
        (['eau', 'oa', 'ow', 'oo', 'ew'], ""),
        (['gue', 'gg', 'gu', 'g'], ""),
        (['dge', 'ge', 'di', 'j'], ""),
        (['rr', 'wr', 'rh', 'r'], ""),
        (['ie', 'eo', 'ae', 'e'], ""),
        (['igh', 'uy', 'ye', 'is'], ""),
        (['augh', 'oor', 'ore', 'oar'], ""),
        (['tch', 'tu', 'ti', 'te'], ""),
        (['dd', 'ed', 'd'], ""),
        (['tt', 'th', 't'], ""),
        (['w', 'u', 'o'], ""),
        (['zz', 'ze', 'z'], ""),
        (['ai', 'au', 'a'], ""),
        (['ough', 'ho', 'aw'], ""),
        (['uoy', 'oi', 'oy'], ""),
        (['sci', 'sh', 'ci'], ""),
        (['bb', 'b'], ""),
        (['wh', 'h'], ""),
        (['ll', 'l'], ""),
        (['pp', 'p'], ""),
        (['ve', 'v'], ""),
        (['y', 'i'], ""),
        (['ee', 'oe'], ""),
        (['oew', 'ue'], ""),
        (['ir', 'yr'], ""),
        (['eer', 'ier'], ""),
        (['ngue', 'ng'], ""),
        (['ui'], ""),
        (['ou'], ""),
        (['ure'], ""),
        (['si'], ""),
    ]
    """
    def get_encoding_rules(self):
        return []

    def get_case_sensitive_encoding(self):
        return True

    """
    Translation follows the following steps
    - Tokenize Sentence
    - Tag parts of speech
    - Strip any unused parts of speech as defined by the language
    - Encode english
    - Parse syntax
    - Join punctuation
    - Render sentence
    """
    def translate(self, sentence):
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        stripped = self.strip(tagged)
        encoded = self.encode(stripped)
        parsed = self.parse_syntax(encoded)
        joined = self.join_punctuation(parsed)
        sentence = self.render_sentence(joined)

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
        rules = self.get_encoding_rules()
        case_sensitive = self.get_case_sensitive_encoding()
        encoded = []
        common_regex = "(?![^{]*})" # A negative lookahead

        for word in tagged_pos:
            if(random.random() < self.fluency):
                encoded.append((word[0], word[1], "skip_parse"))
                continue
            word_temp = word[0]
            for rule in rules:
                rule0_copy = rule[0]
                if not isinstance(rule0_copy, list):
                    rule0_copy = [rule0_copy]
                rule0_copy.sort(key = lambda s : -len(s))
                for r in rule0_copy:
                    pattern = r + common_regex
                    word_temp = re.sub(pattern, "{" + rule[1] + "}", word_temp, flags=re.IGNORECASE)

            # This will strip out any {} in the word, which we use to prevent duplicate encoding
            word_temp = word_temp.replace("{", "").replace("}", "")

            if word[0][0].isupper() and case_sensitive:
                word_temp = word_temp.capitalize()
            encoded.append((word_temp, word[1]))

        return encoded

    def join_punctuation(self, tagged_pos):
        words = []

        for i in range(len(tagged_pos)):
            word = tagged_pos[i]
            word_temp = word[0]
            if word[1] in [".", ":", ","] and i > 0:
                words[-1] = (words[-1][0] + word[0], words[-1][1])
                continue

            words.append((word_temp, word[1]))

        return words

    """
    If not overridden, just returns a join of the words in the tagged_pos
    """
    def parse_syntax(self, tagged_pos):
        return tagged_pos

    def check_parse_skip(self, word):
        if len(word) > 2 and word[2] == "skip_parse":
            return True
        return False

    def render_sentence(self, tagged_pos):
        return " ".join([word[0] for word in tagged_pos])
