from math import sqrt
def factorization(num):
    prime = 2
    ans = []
    root = sqrt(num)
    while num != 1:
        if prime > root:
            ans.append(int(num))
            return ans
        if num % prime == 0:
            ans.append(prime)
            num = num / prime
            root = sqrt(num)
        else:
            if prime == 2:      #tento blok říká, že pokud jsme dělili číslem 2,
                prime = 3       #další máme zvolit číslo 3, jinak skáčeme o 2 čísla
            else:               #(nemá smysl testovat sudá čísla)
                prime += 2
    return ans

if __name__ == "__main__":
    num = int(input("Vložte číslo, jehož faktorizaci chcete provést.\n"))
    
    print(factorization(num))
    input()
