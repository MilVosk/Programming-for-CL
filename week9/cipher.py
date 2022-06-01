def decipher(msg, perm):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if ' ' in msg:
        lists = msg.split(' ')
        letters = list(lists[0])
        letters1 = list(lists[1])
        counter = 0
        res = []
        results = ""
        for i in letters:
            if i in perm:
                index = perm.find(i)
                res.append(alphabet[index])
        counter = counter + 1
        results = ''.join(res)
        counter1 = 0
        res1 = []
        results1 = ""
        for i in letters1:
            if i in perm:
                index = perm.find(i)
                res1.append(alphabet[index])
        counter1 = counter1 + 1
        results1 = ''.join(res1)
        return results + ' ' + results1
    else:
        letters2 = list(msg)
        counter2 = 0
        res2 = []
        results2 = ""
        for i in letters2:
            if i in perm:
                index = perm.find(i)
                res2.append(alphabet[index])
        counter2 = counter2 + 1
        results2 = ''.join(res2)
        return results2
