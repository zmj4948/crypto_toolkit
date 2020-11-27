from ToolKitMain.GCD import gcd


def generators(min_a, n):
    z = {x for x in range(n) if gcd(x, n) == 1}
    for a in range(min_a, n):
        if {pow(a, p) % n for p in range(1, len(z) + 1)} == z:
            yield a

print()