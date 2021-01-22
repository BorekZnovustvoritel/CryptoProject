def squareAndMultiply(base, exponent, modulus):
    exponent = bin(exponent)
    binaryexponent = []
    for i in range(2, len(exponent)): #interval je od čísla 2, binár v Pythonu začína znaky '0b'
        binaryexponent.append(int(exponent[i]))

    ans = base % modulus
    for i in range(1, len(binaryexponent)): #interval začíná od čísla 1, první jednička nic nedělá
        if binaryexponent[i] == 1:
            ans = ((base * ans * ans) % modulus)
        else:
            ans = ((ans * ans) % modulus)
    return ans

if __name__ == "__main__":
    base = int(input("\nZadejte základ pro mocnění: "))
    exponent = int(input("Zadejte exponent: "))
    modulus = int(input("Zadejte modulo: "))
    print(squareAndMultiply(base, exponent, modulus))
    
    input()
