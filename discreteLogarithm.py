def DisLog(a, b, n):
    iteratedNumbers = []
    left = a
    right = b
    ans = 1
    while (left != right):
        right *= b
        ans += 1
        right = right % n
        for i in iteratedNumbers:
            if i == right:
                return "Neexistuje řešení."
        iteratedNumbers.append(right)
    return ans

if __name__ == "__main__":
    print("a = b^x (mod n)")
    a = int(input("Zadejte a: "))
    b = int(input("Zadejte b: "))
    n = int(input("Zadejte n: "))
    ans = DisLog(a, b, n)
    print(ans)
    input()
