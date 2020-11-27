from ToolKitMain.sqrAndMul import square_and_mul


def encryption(x, e, n):
    x = x ** e
    x = x % n
    return x


def decryption(y, d, n):
    return square_and_mul(y, d, n)

print(encryption(8827, 11843, 35461*21799))