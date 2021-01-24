from primeTest import primeTest
def factorizationOnce(inp):
    ans = [1]
    prime = 2
    while inp != 1:
        if inp % prime == 0 and ans[-1] != prime:   #jestliže je na posledním místě prime, nezapisuj ho
            ans.append(prime)
            inp = inp // prime
        elif inp % prime == 0:
            inp = inp // prime
        else:
            if prime == 2:      #tento blok říká, že pokud jsme dělili číslem 2,
                prime = 3       #další máme zvolit číslo 3, jinak skáčeme o 2 čísla
            else:               #(nemá smysl testovat sudá čísla)
                prime += 2
    ans.remove(1)   #jednicka nesmí zůstat v rozkladu, jinak by bylo phi 0
    return(ans)

def nonPrimePhi(num, factInp):
    numerator = 1
    nominator = 1
    for primeN in factInp:
        nominator *= primeN
        numerator *= (primeN - 1)
    ans = num // nominator
    ans *= numerator
    return ans

def phi(num):
    if primeTest(num):
        return (num - 1)
    else:
        return (nonPrimePhi(num, factorizationOnce(num)))
            
if __name__ == "__main__":
    num = int(input("Vložte číslo, jehož funkci Fí chcete zjistit.\n"))
    print(phi(num))
    
    input()
