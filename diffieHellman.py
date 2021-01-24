from random import randint
from discreteLogarithm import disLog
from squareAndMultiply import squareAndMultiply
from groups import getElementDegree

def crack(g, mod, A, B):
    a = disLog(A, g, mod)
    return squareAndMultiply(B, a, mod)

def setKey(g, mod, a = None, b = None):
    q = getElementDegree(g, mod)
    if not a:
        a = randint(2, q)
    A = squareAndMultiply(g, a, mod)
    if not b:
        b = randint(2, q)
    B = squareAndMultiply(g, b, mod)
    keyA = squareAndMultiply(B, a, mod)
    keyB = squareAndMultiply(A, b, mod)
    return a, b, A, B, keyA, keyB

if __name__ == "__main__":
    mode = int(input("Zadejte kód operace:\n'1' pro vytvoření klíče\n'2' pro prolomení\n"))
    if mode == 1:
        g = int(input("Zadejte hodnotu prvku: "))
        mod = int(input("Zadejte prvočíselné modulo grupy: "))
        try:
            a = int(input("Zadejte hodnotu a (Nechte prázdné pro náhodně zvolené a): "))
        except ValueError:
            a = None
        try:
            b = int(input("Zadejte hodnotu b (Nechte prázdné pro náhodně zvolené b): "))
        except ValueError:
            b = None
        a, b, A, B, keyA, keyB = setKey(g, mod, a, b)
        print("a = %d, b = %d, A = %d, B = %d, keyA = %d, keyB = %d" % (a, b, A, B, keyA, keyB))
    elif mode == 2:
        g = int(input("Zadejte prvek g: "))
        mod = int(input("Zadejte prvočíselné modulo grupy: "))
        A = int(input("Zadejte A: "))
        B = int(input("Zadejte B: "))
        print("Klíč je: "+str(crack(g, mod, A, B)))
