import math
import numpy as np


def perm(n):
    top = math.factorial(365)
    bottom = math.factorial(365-n)
    return top / bottom


def birthday(n):
    calc = perm(n) / (365**n)
    return 1 - calc


def birthday_no_collision(n):
    return perm(n) / (365**n)


def hash_check_before_collision(n, y):
    sqrt= math.sqrt(np.log(1/(1-y)))
    two = 2**((n+1)/2)
    return two * sqrt


print(birthday(18))

print(hash_check_before_collision(64, .1))


