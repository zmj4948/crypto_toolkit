def square_and_mul(x, power, m):
    r = x
    binary_of_power = bin(power)[2:]
    for bit in range(1, len(binary_of_power)):
        r = pow(r, 2) % m
        if binary_of_power[bit] == '1':
            r = r * x % m
    return r


def operations_counter(power):
    """
    prints out the num of operations for the current power
    """
    squares = 0  # counter for num of squares
    mult = 0  # counter for num of mults
    binary_of_power = bin(power)[2:]
    print(binary_of_power)
    for bit in range(1, len(binary_of_power)):
        squares += 1  # we square for each bit
        if binary_of_power[bit] == '1':  # only if bit == 1
            mult += 1  # we mult
    print('squares:' + str(squares))
    print('mults:' + str(mult))
    print('total: ' + str(squares + mult))
