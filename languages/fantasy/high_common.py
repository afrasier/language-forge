from languages.base_language import BaseLanguage

class HighCommon(BaseLanguage):

    """
    These fancy guys don't use plosives
    """
    def get_encoding_rules(self):
        return [
            (["ed"], "et"),
            (["ff", "ph", "gh", "lf", "ft"], "f"),
            (["g", "gg", "gh", "gu", "gue"], "hu"),
            (["h", "wh"], "ch"),
            (["j", "ge", "g", "dge", "di", "gg"], "ü"),
            (["k", "fo", "c", "ch", "cc", "lk", "qu", "q", "ck", "x", "oo"], "uch"),
            (["l", "ll"], "yl"),
            ("do", "tun"),
            (["mm", "mb", "mn", "lm"], "khm"),
            (["nn", "kn", "gn", "pn"], "khn"),
            (["p", "pp"], ""),
            (["r", "rr", "wr", "rh"], "rh"),
            (["s", "c", "sc", "ps", "st", "ce", "se"], "s"),
            (["tt", "th", "ed"], "'"),
            (["v", "f", "ph", "ve"], "f"),
            (["z", "zz", "s", "ss", "x", "ze", "se"], "ß"),
            (["ai", "eigh", "aigh", "ay", "er", "et", "ei", "au", "ea", "ey"], "aí"),
            (["ea", "u", "ie", "ai", "a", "eo", "ei", "ae", "ay"], "e"),
            (["ee", "ea", "y", "ey", "oe", "ie", "i", "ei", "eo", "ay"], "ë"),
            (["e", "ui", "y", "ie"], "i"),
            (["i", "y", "igh", "ie", "uy", "ye", "ai", "is", "eigh"], "eí"),
            (["ho", "au", "aw", "ough"], "ko"),
            (["a", "er", "i", "ar", "our", "or", "e", "ur", "re", "eur"], "ur"),
            (["air", "are", "ear", "ere", "eir", "ayer"], "aih"),
            (["a", "ar", "au", "er", "ear"], "eih"),
            (["ure", "our"], "du"),
            (["s", "si", "z"], "se"),
            (["th"], "da"),
            (["ng", "n", "ngue"], "aif"),
            ("w", "h")
        ]

    def parse_syntax(self, tagged_pos):
        words = []

        for word in tagged_pos:
            if self.check_parse_skip(word):
                words.append(word)
                continue
            word_temp = word[0]
            if word[1] == "PRP" and len(word_temp) > 0:
                word_temp = word_temp[0] + "ist"

            words.append((word_temp, word[1]))

        return words
