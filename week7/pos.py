#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Programming for Computational Linguistics 2020/2021
    OOP -- exercises
    Exercise 4
"""

from builder import *

def get_unique_pos(filename, builder):
    new= []
    results = []
    list_ = []
    for line in open(filename, "r"):
        line = line.strip()
        #print(line)
        if line == "":
            continue
        else:
            #print(i)
            j = 0
            k = 0
            res = line.split()
            results.append((res[3]))
            k = k + 1

    for pos in results:
        if pos not in new:
            new.append(pos)

        # this is the place where we use the builder
        # the cool part is that we don't care what is the format of the file we read
    tok = builder.buildToken(line)

        ### HERE -- finish this code
        ### you should use 'tok' and 'result'
#print(len(new))
    return new
def build_builder(filename):
    if filename.endswith("conllu"):
        builder = ConLLUTokenBuilder()
    elif filename.endswith("conll09"):
        builder = ConLL09TokenBuilder()
    else:
        raise RuntimeError("Unknown file format: " + filename)

    return builder


## here the main part starts
#filename = "small_train.conllu"
#builder = build_builder(filename)

#unique_pos = get_unique_pos(filename, builder)
#print("Nr of unique POS (should be 10):", unique_pos)
