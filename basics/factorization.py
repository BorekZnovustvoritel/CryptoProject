from math import sqrt
from time import perf_counter
def factorization(num):
    ans = []
    while num % 2 == 0:
        num = num // 2
        ans.append(2)
    prime = 3
    root = sqrt(num)
    while num != 1:
        if prime > root:
            ans.append(int(num))
            return ans
        if num % prime == 0:
            ans.append(prime)
            num = num // prime
            root = sqrt(num)
        else:
            prime += 2
            if prime > root:
                break
    if num != 1:
        ans.append(num)
    return ans

if __name__ == "__main__":
    num = int(input("Vložte číslo, jehož faktorizaci chcete provést.\n"))
    ref = perf_counter()
    print(factorization(num))
    print("Operace zabrala %.4f sekund" % (perf_counter() - ref))
    input()
