import operator
import pprint
def most_common(i):
    m = max(i.items(), key=operator.itemgetter(1))[0]
    #print(m)
    return(m)
most_common({"NOUN": 2, "VERB": 1})

def read_conllu(i):
    f = open(i)
    results = []
    i = 0
    j = 0
    for line in f:
        line = line.strip()
        if not line:  # line is blank
            continue
        else:
            #print(i)
            j = 0
            res = line.split()
            results.append((res[1], res[3]))
            i = i + 1
    #print(results)
    return results

#read_conllu("small_train.conllu")

def train_and_tag(train_file, test_words):
    f = open(train_file)
    d = {}
    results = []
    test_ = []
    for i in test_words:
        g = i.lower()
        test_.append(g)
    print(test_)
    for line in f:
        line = line.strip()
        if not line:  # line is blank
            continue
        else:
            #j = 0
            res = line.split()
            results.append((res[1].lower(), res[3]))

            small = res[1].lower()

            if small not in d:
                # create d[small] if not in yet and initialize it with one
                d[small] = {}
                d[small][res[3]] = 1
            elif small in d:
                if res[3] in d[small]:
                    d[small][res[3]] = d[small][res[3]] + 1
                else:
                    d[small][res[3]] = 1
            x = d[small]
            m = ""
            #print(d[small]
            m = most_common(d[small])
            d_final = {}
            #print(d)
            list = []
            #print(d[small])
    for i in test_:
        if i in d.keys():
            print(i)
            #d_final[g] = d[g]
            m = most_common(d[i])
            list.append(m)

        elif i not in d.keys():
            list.append("UNK")

    #print(list)
    return list

    #print(d)
    #return d
#train_and_tag("en_gold.conllu", [ "The", "citizens", "hate", "weapons", "but", "love", "Christmas" ])
