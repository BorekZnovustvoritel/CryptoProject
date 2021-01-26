from random import randint
from primeTest import primeTest

def primeGen(bitLength):
    prime = randint(2**(bitLength-1), 2**(bitLength) - 1)
    while not primeTest(prime):
        prime = randint(2**(bitLength-1), 2**(bitLength) - 1)
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