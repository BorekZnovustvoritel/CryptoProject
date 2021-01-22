import time

def DisLog(a, b, n, timeLimit):
    iteratedNumbers = []
    left = a
    right = b
    ans = 1
    ref = time.perf_counter()
    while (left != right):
        right *= b
        ans += 1
        right = right % n
        for i in iteratedNumbers:
            if i == right:
                return "Neexistuje řešení.", time.perf_counter() - ref
        iteratedNumbers.append(right)
        if (time.perf_counter() - ref) >= timeLimit :
            return "Časový limit úlohy vypršel.", time.perf_counter() - ref
    return ans, time.perf_counter() - ref

if __name__ == "__main__":
    print("a = b^x (mod n)")
    a = int(input("Zadejte a: "))
    b = int(input("Zadejte b: "))
    n = int(input("Zadejte n: "))
    ans, time = DisLog(a, b, n, 15)
    print(ans, "\nČas dokončení úlohy: ", time, "s")
    input()
