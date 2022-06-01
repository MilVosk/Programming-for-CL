def find_opposites(lst):
    var = []
    new = []
    s = set(lst)
    for i in s:
        r = i[::-1]
        if r in s and lst.index(i) > lst.index(r):
            var.append(i)
            var.append(r)
            pair = tuple(var[::-1])
            new.append(pair)
        var = []

    return new

