from random import randint
from basics.primeTest import millerRabin as primeTest

def primeGen(bitLength):
    if bitLength < 2:
        raise ValueError("No prime numbers exist in given range.")
    prime = randint(2**(bitLength-1), 2**(bitLength) - 1)
    if prime % 2 == 0:
        prime += 1
    while not primeTest(prime):
        prime = randint(2**(bitLength-1), 2**(bitLength) - 1)
        if prime % 5 == 0:
            continue
    return prime

def primeFrom(start, stop):
    prime = randint(start, stop)
    while not primeTest(prime):
        prime = randint(start, stop)
    return prime

if __name__ == "__main__":
    length = int(input("Zadejte bitovou délku prvočísla: "))
    print(primeGen(length))

    input()