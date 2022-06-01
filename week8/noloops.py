import numpy as np
def product(nums):
    if nums == 0:
        return 1
    else:
        #print(np.prod(nums))
        return np.prod(nums)
product([2, 3, 1, -5, 3])

def squares(nums):
    if nums == 0:
        return 1
    else:
        array = np.array(nums)
        result = array * array
        #print(list(result))
        return list(result)
squares([-2, -1, 0, 1, 2, 5])

def num_zeros(n):
    return str(n).count('0')
num_zeros(100200304501)
