from collections import Counter
def can_be_composed(word1, word2):

    can_be_composed = True
    result_word1 = word2dict(word1)
    result_word2 = word2dict(word2)
    #print(result_word1)
    #print(result_word2)
    A = list(result_word1.keys())
    B = list(result_word2.keys())
    commonKeys = set(A) - (set(A) - set(B))

    for key in result_word1.keys():

        if key not in result_word2.keys():

            can_be_composed = False
    for key in commonKeys:
        if(result_word1[key] > result_word2[key]):
            #print(result_word1[key])
            #print(result_word2[key])
            can_be_composed = False

    #print(can_be_composed)
    return can_be_composed

def word2dict(word):
    dictionary = dict(Counter(word))
    return dictionary

can_be_composed("uqyki", "vovr")
