def euklides(a, b):
    while (a != 0 and b != 0):
        if (a > b):
            a = a % b
        else:
            b = b % a
    if (a == 0):
        return b
    else:
        return a

if __name__ == "__main__":
    a = int(input("Zadejte 1. číslo: "))
    b = int(input("Zadejte 2. číslo: "))
    print(euklides(a, b))

    input()
