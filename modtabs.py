from GCD import gcd


def modTabs(num):
    print("     ", end=" ")
    for i in range(0, num):
        print(i, end="  "),
    print("")
    for side in range(1, num):
        print(str(side) + "|   ", end=" ")
        for i in range(0, num):
            current = (side ** i ) % num
            print(current, end="  ")
        print("")


modTabs(18)
