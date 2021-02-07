from basics.euklidesAlgorithm import euklides as GCD
from basics.eulerPhi import phi
from basics.squareAndMultiply import squareAndMultiply

def inverse(num, mod):
    if GCD(num, mod) != 1:
        raise ValueError("Neexistuje inverzní prvek.")
    else:
        exp = phi(mod) - 1
        #print("exp = "+str(exp))
        ans = squareAndMultiply(num, exp, mod)
    return ans

def extendedEuklides(num, mod):
    row1 = [mod, num]
    row2 = [None]
    numOfLines = 1 #Na konci bychom museli ubrat nulový řádek, tak číslo snížíme již teď
    while row1[-1] != 0:
        row2.append(row1[-2] // row1[-1])
        row1.append(row1[-2] % row1[-1])
        numOfLines += 1
    row1.remove(0)
    if row1[-1] != 1:
        raise ValueError("Neexistuje inverzní prvek.")
    reverseRow3 = [0, 1]
    for i in range(numOfLines - 2, 0, -1):
        reverseRow3.append(reverseRow3[-1] * row2[i] +reverseRow3[-2] )
    a = reverseRow3[-1]
    b = reverseRow3[-2]
    if ((a * num) - (b * mod)) == -1:
        a = -a % mod
    return a

if __name__ == "__main__":
    alg = int(input("Zadejte kód algoritmu:\n1) Eulerova věta\n2)Rozšířený Euklidův algoritmus\n"))
    num = int(input("Zadejte číslo, jehož inverzní prvek chcete zjistit: "))
    mod = int(input("Zadejte modulo: "))
    if alg == 1:
        print(inverse(num, mod))
    elif alg == 2:
        print(extendedEuklides(num, mod))
    input()
