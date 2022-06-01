def find_maxima(lst):
    maxima = []
    maxima.append(lst[0])
    for i in lst:
        if i > maxima[-1]:
            maxima.append(i)
        elif i <= maxima[-1]:
            continue
    return maxima
