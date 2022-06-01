import math
l = []
def last(l):
    for i in list(l):
        print(l[-1])
        return l[-1]
        break
#last([1, 2, 5, 4])

x = [9, 8, 10, 6, 7, 6, 4]
def middle(l):
    m = int(len(l) / 2)
    x = l[m]
    print(x)
    return x
middle(x)

def product(l):
    for i in list(l):
        new_value = list()
        result = 1
        for answers in list(l):
                result = result * answers
    print(result)
    return result
#product([1, 2, 3, 4, 5])

def mean(l):
    m = sum(l) / len(l)
    print(m)
    return m
#mean([1, 2, 3, 4])
def even_sum(l):
    even = []
    for i in range(0, len(l)):
        if i % 2:
            pass
        else :
            even.append(l[i])
    print(sum(even))
    return sum(even)
#even_sum([71, 95, 4, 7, 19])
