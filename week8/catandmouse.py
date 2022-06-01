from constituents import *

sent = Phrase(phrase_type = 'S', children = [Phrase(phrase_type = 'NP', children = [Token("DT", "The"), Token("NN", "cat")]), Phrase(phrase_type = 'VP', children = [Token("VB", "chases"), Phrase(phrase_type = 'NP', children = [Token('DT', 'the'), Token('NN', 'mouse')])]), Token("PUNCT", ".")])

#print(sent)
