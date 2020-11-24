def alice_bigA(p, fish, a):
    return (fish ** a) % p


def common_secret(fish, big, p, little):
    return (fish ** (big*little)) % p
