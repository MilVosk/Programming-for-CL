
class ConLLToken(object):
    def __init__(self, form, lemma, pos, morph):
        self.form = form
        self.lemma = lemma
        self.pos = pos
        self.morph = morph

    def __str__(self):
        toks = [ self.form, self.lemma, self.pos, self.morph]
        return "" + ",".join(toks) + ""

    def is_punctuation(self):
        return True if self.pos == "PUNCT" else False

    def is_inflected(self):
        return False if self.lemma.lower() == self.form.lower() else True

    def get_person(self):
        if "Person" in self.morph:
            array = []
            array = self.morph.split("|")
            value = []
            for i in array:
                if "Person" in i:
                    value = i.split("=")
            return value[1]

tok1 = ConLLToken("comes", "come", "VERB", "Mood=Ind|Number=Sing|Person=3")
tok2 = ConLLToken ("year", "year", "NOUN", "Number=Sing")
tok3 = ConLLToken(",", ",", "PUNCT", "_")
#print("Token 1:", str(tok1 ))
#print("Token 2:", tok2)
#print("Punctuation?", tok1.is_punctuation (), tok2.is_punctuation (), tok3.is_punctuation ())
#print("Inflected?", tok1.is_inflected (), tok2.is_inflected (), tok3.is_inflected ())
#print("Person?", tok1.get_person(), tok2.get_person(), tok3.get_person())
