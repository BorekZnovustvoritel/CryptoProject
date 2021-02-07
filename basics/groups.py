from basics.eulerPhi import phi, factorizationOnce
from basics.squareAndMultiply import squareAndMultiply

def getElementDegree(num, mod):
    groupDegree = phi(mod)
    factors = factorizationOnce(groupDegree)
    for i in range(len(factors)-1, -1, -1):
        exponent = groupDegree//factors[i]
        if squareAndMultiply(num, exponent, mod) == 1:
            return exponent
    return groupDegree

if __name__ == "__main__":
    mod = int(input("Zadejte modulo grupy: "))
    num = int(input("Zadejte prvek grupy: "))
    print("Řád prvku %d grupy modulo %d je %d" % (num, mod, getElementDegree(num, mod)))

    input()
