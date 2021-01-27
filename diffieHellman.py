from random import randint
from discreteLogarithm import disLog
from squareAndMultiply import squareAndMultiply
from groups import getElementDegree
from primeGen import primeGen

def crack(g, mod, A, B):
    a = disLog(A, g, mod)
    return squareAndMultiply(B, a, mod)

def setKey(g = None, modLength = None, mod = None, a = None, b = None):
    if not mod:
        if not modLength:
            modLength = 2048
        print("Generování prvočísla o délce %d bitů..." % modLength)
        mod = primeGen(modLength)
        print("Hotovo!")
    if not g:
        g = randint(2, mod - 1)
    if modLength < 124:
        q = getElementDegree(g, mod)
    else:
        q = g
    if not a:
        a = randint(2, q)
    A = squareAndMultiply(g, a, mod)
    if not b:
        b = randint(2, q)
    B = squareAndMultiply(g, b, mod)
    keyA = squareAndMultiply(B, a, mod)
    keyB = squareAndMultiply(A, b, mod)
    return mod, g, a, b, A, B, keyA, keyB

if __name__ == "__main__":
    mode = int(input("Zadejte kód operace:\n'1' pro vytvoření klíče\n'2' pro prolomení\n"))
    if mode == 1:
        try:
            g = int(input("Zadejte hodnotu prvku (Nechte prázdné pro náhodně zvolené g): "))
        except ValueError:
            g = None
        try:
            mod = int(input("Zadejte prvočíselné modulo grupy (Nechte prázdné pro náhodně zvolené modulo): "))
            modLength = None
        except ValueError:
            mod = None
            try:
                modLength = int(input("Zadejte bitovou délku modula grupy (Nechte prázdné pro délku 2048 b): "))
            except ValueError:
                modLength = None
        try:
            a = int(input("Zadejte hodnotu a (Nechte prázdné pro náhodně zvolené a): "))
        except ValueError:
            a = None
        try:
            b = int(input("Zadejte hodnotu b (Nechte prázdné pro náhodně zvolené b): "))
        except ValueError:
            b = None
        mod, g, a, b, A, B, keyA, keyB = setKey(g, modLength, mod, a, b)
        print("mod = %d\ng = %d\na = %d\n b = %d\n A = %d\n B = %d\n keyA = %d\n keyB = %d" % (mod, g, a, b, A, B, keyA, keyB))
    elif mode == 2:
        g = int(input("Zadejte prvek g: "))
        mod = int(input("Zadejte prvočíselné modulo grupy: "))
        A = int(input("Zadejte A: "))
        B = int(input("Zadejte B: "))
        print("Klíč je: "+str(crack(g, mod, A, B)))

    input()
