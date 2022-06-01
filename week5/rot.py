def rotated(lst, n):
    a = []
    a = lst
    test_list = []
    #if n < 0:
    # using list comprehension to left rotate by -n
    test_list = [lst[(i + n) % len(lst)]for i, x in enumerate(lst)]

        #print(test_list)
    #return test_list
    #elif n > 0:
    # using list comprehension to right rotate by n
    test_list = [lst[(i - n) % len(lst)]for i, x in enumerate(lst)]
        #print(test_list)
        #return test_list
    #elif n == 0:
    test_list = [lst[(i + n) % len(lst)]for i, x in enumerate(lst)]
    #print(test_list)
    return test_list
    #print(test_list)
rotated(['B', 7, 'A'], -1)
