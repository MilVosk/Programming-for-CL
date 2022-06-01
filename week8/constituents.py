#from catandmouse import *
class Token(object):
    def __init__(self, pos, word):
        self.pos = pos
        self.word = word
        self.var = '({self.pos}, {self.word})'.format(self=self)
    def __repr__(self):

        return self.var

    def __str__(self):
        self.final = str(self.var).replace(',', '')
        return self.final


t_the = Token('DT', 'The')
t_cat = Token('NN', 'cat')
vb_chases = Token('VB', 'chases')
dt_the = Token('DT', 'the')
t_mouse = Token('NN', 'mouse')
p_punct = Token('PUNCT', '.')
#p_the_cat = Phrase('NP', [t_the , t_cat ])
#print(str(t_the))
#print(str(t_cat))
#print(str(vb_chases))


class Phrase(object):
    def __init__(self, phrase_type, children):
        self.phrase_type = phrase_type
        self.children = children
        self.ret = '({self.phrase_type}, {self.children}'.format(self=self)

    def __repr__(self):
        return self.ret

    def __str__(self):
        self.list = str(self.ret).replace('[', '').replace(']', ')').replace(',', '')
        #if len(self.children) > 1:

        return self.list


#p_the_cat = Phrase('NP', [t_the, t_cat])
#print(p_the_cat)
p_vb_chases= Phrase('NP', vb_chases)
#print(p_vb_chases)
#var = Phrase(phrase_type = 'NP', children = [Token("DT", "The"), Token("NN", "cat")])
#print(var)
Phrase(phrase_type = 'VP', children = [Token("VB", "chases")])
#Phrase(phrase_type = 'NP', children = [Token('DT', 'the'), Token('NN', 'mouse')])
Phrase(phrase_type = 'S', children = [Phrase(phrase_type = 'NP', children = [Token("DT", "The"), Token("NN", "cat")]), Phrase(phrase_type = 'VP', children = [Token("VB", "chases")]), Phrase(phrase_type = 'NP', children = [Token('DT', 'the'), Token('NN', 'mouse')]), Token("PUNCT", ".")])
