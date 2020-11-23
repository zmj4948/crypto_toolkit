from ToolKitMain.GCD import gcd
import random
from ToolKitMain.sqrAndMul import square_and_mul


def fermat_test(n, k):
    for i in range(k):
        a = random.randint(2, n - 2)
        if gcd(a, n) == 1:
            if square_and_mul(a, n - 1, n) != 1:
                return False
    return True
