import re
import math
a = ""
def positivize(review):
    a = review
    g = a.split()
    for s in g:
        if s.isdigit():
            #print(s)
            if g[g.index(s) + 1] == "minutes":
                i = int(s)
                k = math.floor(i/2)
                      #print(k)
                j = str(k)
                      #print(type(j))
                      #print(j)
                a = a.replace(s, "only {}" .format(j))
        elif s == "frozen":
          a = a.replace("frozen", "farm-fresh", 1)
        elif s == "Frozen":
            a = a.replace("Frozen", "Farm-fresh", 1)
        elif s == "horrible":
            a = a.replace("horrible", "fantastic", 1)
        elif s == "Horrible":
            a = a.replace("Horrible", "Fantastic", 1)
        elif s == "bad":
          a = a.replace("bad", "good", 1)
        elif s == "Bad":
          a = a.replace("Bad", "Good", 1)
        elif s == "dirty":
          a = a.replace("dirty", "clean", 1)
        elif s == "Dirty":
          a = a.replace("Dirty", "Clean", 1)
        elif s == "disgusting":
          a = a.replace("disgusting", "sublime", 1)
        elif s == "Disgusting":
          a = a.replace("Disgusting", "Sublime", 1)
        elif s == "expensive":
          a = a.replace("expensive", "affordable", 1)
        elif s == "Expensive":
          a = a.replace("Expensive", "Affordable", 1)
        elif s == "moldy":
          a = a.replace("moldy", "flavourful", 1)
        elif s == "Moldy":
          a = a.replace("Moldy", "Flavourful", 1)
    return a

positivize(" 1 time I went there. They serve 57 dishes. The food tasted expensive .")
