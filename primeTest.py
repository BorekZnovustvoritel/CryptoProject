from random import randint
#try:
from squareAndMultiply import squareAndMultiply
#except ImportError:
    #print("Missing an important module: squareAndMultiply.py")
def millerRabin(num, maxIter):
    if (num % 2) == 0:
        return False
    part = num - 1
    s = 0
    while (part % 2) == 0:
        part = part // 2
        s += 1
    r = part
    iMax = s - 1
    print("s="+str(s)+", r="+str(r))
    bases = []
    iterNum = 1
    while (iterNum < maxIter) and (iterNum <= num - 3):
        base = randint(2, num - 2)
        if base in bases:
            continue
        else:
            bases.append(base)
            iterNum += 1
            temp = squareAndMultiply(base, r, num)
            if temp == 1 or temp == num - 1:
                continue
            else:
                subAns = False
                for i in range(1, iMax+1):
                    temp = squareAndMultiply(base, r*(2**i), num)
                    if temp == num - 1:
                        subAns = True
                        break
                if not subAns:
                    #print(bases)
                    return False
    #print(bases)
    return True

def lucasLehmer(num):
    part = num + 1
    ref = 2
    exp = 1
    while part > ref:
        exp += 1
        ref *= 2
    if ref != part:
        raise ValueError("Given number cannot be tested with Lucas-Lehmer's test.")
    u = 4
    for i in range(1, exp - 1):
        u = (u**2 - 2) % num
    if u == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    alg = int(input("Zadejte 1 pro Miller-Rabinův test, 2 pro Lucas-Lehmerův test: "))
    if alg == 1:
        num = int(input("Zadejte celé číslo: "))
        maxIter = int(input("Zadejte počet cyklů: "))
        if millerRabin(num, maxIter) == True:
            print("Číslo "+str(num)+" je prvočíslo.")
        else:
            print("Číslo "+str(num)+" není prvočíslo.")
    elif alg == 2:
        num = int(input("Zadejte celé číslo: "))
        if lucasLehmer(num):
            print("Číslo "+str(num)+" je prvočíslo.")
        else:
            print("Číslo "+str(num)+" není prvočíslo.")
    else:
        print("Lmao, nauč se číst.")
    input()