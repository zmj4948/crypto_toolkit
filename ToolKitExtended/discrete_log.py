from ToolKitMain.sqrAndMul import square_and_mul


def discrete_log(x, base, mod):
    for i in range(1, mod):
        val = square_and_mul(base, i, mod)
        if val == x:
            return i
    # return 0 if not defined
    return 0


print(discrete_log(7,3,89))
print(discrete_log(3,7,101))