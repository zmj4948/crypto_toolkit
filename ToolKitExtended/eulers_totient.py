from ToolKitMain.GCD import gcd


def phi(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result

p = 35461
q = 21799
print((p-1)*(q-1))