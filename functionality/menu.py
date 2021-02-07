from functionality.inp import inp
from functionality.clear import clear

def menu(head = None, options = None):
    clear()
    if head:
        print(head)
        numOfOptions = 0
    for option in options:
        print(" %d: %s" % (numOfOptions + 1, option))
        numOfOptions += 1
    print(" %d: Exit" % (numOfOptions + 1))
    a = inp(int, "Zadejte číslo zvolené možnosti:\n", "Zkuste to znovu:\n")
    if a > 0 and a <= numOfOptions + 1:
        return a
    else:
        exit = False
        while not exit:
            a = inp(int, "Zkuste to znovu:\n", "Zkuste to znovu:\n")
            if a > 0 and a <= numOfOptions + 1:
                return a

if __name__ == "__main__":
    print(menu(head = "Hlavní menu:", options = ("RSA", "DH", "Basics")))