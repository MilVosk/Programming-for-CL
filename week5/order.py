def sort(words):
    alpha = ['A', 'a', 'Al', 'An', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'Le', 'Lo', 'Louis', 'Louise', 'Lu', 'Luc', 'Luk',
                'M', 'm', 'Ma', 'ma', 'Mi', 'mi', 'N', 'n', 'Na', 'No', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'X', 'x',
                'Y', 'y', 'Z', 'z']

    for j in range(0, len(words)):
        for i in range(0, len(words)):
            _sorted = False
            if i != len(words)-1:
                for k in range(0,len(words[i])):
                    if not _sorted:
                        if k != (len(words[i]) and len(words[i+1])):
                            if alpha.index(words[i][k]) > alpha.index(words[i+1][k]):
                                words[i], words[i+1] = words[i+1], words[i]
                                _sorted = True
                            elif alpha.index(words[i][k]) < alpha.index(words[i+1][k]):
                                _sorted = True
                            else:
                                if len(words[i+1]) < len(words[i]):
                                    words[i], words[i+1] = words[i+1], words[i]
                                    _sorted = True
    #print(words)
    #return words
sort([ 'bat' , 'cat' , 'dog' , 'fish' , 'zebra', 'Marcel' ])
