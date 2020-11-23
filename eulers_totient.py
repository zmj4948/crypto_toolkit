from GCD import gcd


def phi(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result
