from ToolKitMain.sqrAndMul import square_and_mul


def encryption(x, e, n):
    x = math.pow(x, e)
    x = x % n
    return x


def decryption(y, d, n):
    return square_and_mul(y, d, n)
