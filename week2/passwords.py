from fragments import get_random_text
from fragments import txts
from random import choice
import random
import string
def easy_password(i):
    password = ""
    for n in range(i+5):
        target_length = i
        length_pw = len(password)
        fragment = get_random_text()
        length_fragment = len(fragment)
        actual_difference = target_length - length_pw
        future_length = length_pw + length_fragment
        if length_pw < target_length and actual_difference > 1 and future_length <= target_length and future_length != target_length -1 :
            password = password + fragment
        elif length_pw == target_length:
            break
    return password
easy_password(25)
