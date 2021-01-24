from random import randint
from primeTest import primeTest
def primeGen(bitlength):
    prime = randint(2**(bitlength-1), 2**(bitlength) - 1)
    while not primeTest(prime):
        prime = randint(2**(bitlength-1), 2**(bitlength) - 1)
    return prime

if __name__ == "__main__":
    length = int(input("Zadejte bitovou délku prvočísla: "))
    print(primeGen(length))

    input()