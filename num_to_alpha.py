alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']


def alpha_to_ascii(letter):
    return ord(letter)


def ascii_to_alpha(num):
    return chr(num)


def alpha_to_zero(letter):
    return alphabet.index(letter)


def zero_to_alpha(num):
    return alphabet[num]
