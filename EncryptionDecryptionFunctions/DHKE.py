def alice_bigA(p, fish, a):
    return (fish ** a) % p


def common_secret(fish, big, p, little):
    return (big**little) % p

p = 487
fish = 11
a = 355
b = 200
big = alice_bigA(p,fish,a)
print(common_secret(fish, big, p, b))
