from euklidesAlgorithm import euklides as GCD
from eulerPhi import phi
from squareAndMultiply import squareAndMultiply

def inverse(num, mod):
    if GCD(num, mod) != 1:
        raise ValueError("Neexistuje inverzní prvek.")
    else:
        exp = phi(mod) - 1
        print("exp = "+str(exp))
        ans = squareAndMultiply(num, exp, mod)
    return ans

if __name__ == "__main__":
    num = int(input("Zadejte číslo, jehož inverzní prvek chcete zjistit: "))
    mod = int(input("Zadejte modulo: "))

    input()
