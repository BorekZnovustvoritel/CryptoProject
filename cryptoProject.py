import runpy
#^Místo pro základní Python moduly
#try:
from functionality.inp import inp
from functionality.menu import menu
import algorithms.rsa as rsa
import algorithms.diffieHellman as dh
from functionality.stopwatch import stopwatch
import basics
#^Místo pro vlastní moduly
options = ("RSA", "Diffie-Hellman", "Základní operace")
option = menu("Hlavní menu:", options)
while option != len(options) + 1:
    if option == 1:
        #rsa
        Pk = 0
        Sk = 0
        mod = 0
        mess = 0
        encr = 0
        options1 = ("Sestavení", "Zašifrování", "Dešifrování")
        option1 = menu("RSA", options1)
        while option1 != len(options) + 1:
            if option1 == 1:
                #sestavení
                modBitLength = inp(int, "Zadejte bitovou délku modula. Nechte pole prázdné pro modulo délky 2048 b.\n", "", True)
                Pk = inp(int, "Zadejte veřejný klíč. Nechte prázdné pro náhodně zvolený.\n", "", True)
                ans, time = stopwatch(rsa.generate, bitLength = modBitLength, publicKey = Pk)
                mod, Pk, Sk = ans
                print("mod = %d\nPk = %d\nSk = %d\nVýpočet trval %.2f sekund." % (mod, Pk, Sk, time))
                input("Stiskněte enter pro pokračování.")
            elif option1 == 2:
                #zašifrování
                if Pk != 0 and Sk != 0 and mod != 0:
                    options2 = ("Použít hodnoty v paměti", "Vložit vlastní hodnoty\nHodnoty v paměti jsou:\nmod = %d\nPk = %d\nSk = %d" % (mod, Pk, Sk))
                    option2 = menu("RSA - šifrování:", options2)
                    if option2 == 1:
                        #použít uložené hodnoty
                        mess = inp(int, "Zadejte číslo k zašifrování:\n", "Zkuste to znovu:\n")
                        encr = rsa.encrypt(mess, Pk, mod)
                        print("Zašifrované číslo je:\n%d" % encr)
                        input("Stiskněte enter pro pokračování.")
                    elif option2 == 2:
                        #použít nové hodnoty
                        mod = inp(int, "Zadejte modulo kryptosystému:\n", "Zkuste to znovu:\n")
                        Pk = inp(int, "Zadejte veřejný klíč:\n", "Zkuste to znovu:\n")
                        mess = inp(int, "Zadejte číslo k zašifrování", "Zkuste to znovu")
                        encr = rsa.encrypt(mess, Pk, mod)
                        print("Zašifrované číslo je:\n%d" % encr)
                        input("Stiskněte enter pro pokračování.")
                else:
                    #použít nové hodnoty
                    mod = inp(int, "Zadejte modulo kryptosystému:\n", "Zkuste to znovu:\n")
                    Pk = inp(int, "Zadejte veřejný klíč:\n", "Zkuste to znovu:\n")
                    mess = inp(int, "Zadejte číslo k zašifrování", "Zkuste to znovu")
                    encr = rsa.encrypt(mess, Pk, mod)
                    print("Zašifrované číslo je:\n%d" % encr)
                    input("Stiskněte enter pro pokračování.")
            elif option1 == 3:
                #dešifrování
                if Pk != 0 and Sk != 0 and mod != 0:
                    options2 = ("Použít hodnoty v paměti", "Vložit vlastní hodnoty\nHodnoty v paměti jsou:\nmod = %d\nPk = %d\nSk = %d" % (mod, Pk, Sk))
                    option2 = menu("RSA - dešifrování:", options2)
                    if option2 == 1:
                        #použít uložené hodnoty
                        tempEncr = inp(int, "Zadejte číslo k dešifrování. Nechte prázdné pro použití zprávy z paměti.\nZašifrované zpráva v paměti:\n%d\n" % encr, "", True)
                        if tempEncr:
                            encr = tempEncr
                        mess = rsa.decrypt(encr, Sk, mod)
                        print("Dešifrovaná zpráva je:\n%d" % mess)
                        input()
                    elif option2 == 2:
                        #použít nové hodnoty
                        mod = inp(int, "Zadejte modulo kryptosystému:\n", "Zkuste to znovu:\n")
                        Sk = inp(int, "Zadejte soukromý klíč:\n", "Zkuste to znovu:\n")
                        encr = inp(int, "Zadejte číslo k dešifrování", "Zkuste to znovu")
                        mess = rsa.decrypt(encr, Sk, mod)
                        print("Dešifrovaná zpráva je:\n%d" % encr)
                        input("Stiskněte enter pro pokračování.")
                
            option1 = menu("RSA", options1)
    elif option == 2:
        #dh
        modLength = 0
        mod = 0
        generator = 0
        a = 0
        b = 0
        A = 0
        B = 0
        keyAlice = 0
        keyBob = 0
        mod = inp(int, "Zadejte prvočíselné modulo grupy (Nechte prázdné pro náhodně zvolené modulo): ", "Zkuste to znovu: ", skipable=True)
        if not mod:
            modLength = inp(int, "Zadejte bitovou délku modula grupy (Nechte prázdné pro délku 2048 b): ", "Zkuste to znovu: ", skipable=True)
        g = inp(int, "Zadejte hodnotu prvku (Nechte prázdné pro náhodně zvolené g): ", "Zkuste to znovu: ", skipable = True)
        g = g % mod
        a = inp(int, "Zadejte hodnotu a (Nechte prázdné pro náhodně zvolené a): ", "Zkuste to znovu: ", skipable = True)
        a = a % mod
        b = inp(int, "Zadejte hodnotu b (Nechte prázdné pro náhodně zvolené b): ", "Zkuste to znovu: ", skipable = True)
        b = b % mod
        ans, time = stopwatch(dh.setKey, g = g, modLength = modLength, mod = mod, a = a, b = b)
        mod, g, a, b, A, B, keyA, keyB = ans
        print("Bylo zvoleno:\nmod = %d\ng = %d\nAlice vygenerovala a = %d\nBob vygeneroval b = %d\nAlice poslala A = %d\nBob poslal B = %d\nAlice získala klíč: %d\nBob získal klíč: %d\nOperace trvala %.3f sekund" % (mod, g, a, b, A, B, keyA, keyB, time))
        input("Stiskněte enter pro pokračování.")


    elif option == 3:
        #basics
        options1 = ("Diskrétní logaritmus", "Největší společný dělitel dvou čísel")
        option1 = menu("Basics", options1)
        if option1 == 1:
            #DisLog
            print("Diskrétní logaritmus hledá číslo x, pro které platí rovnice ve tvaru: a = b^x (mod n).")
            a = inp(int, "Zadejte a (Výsledek modulárního mocnění): ")
            b = inp(int, "Zadejte b (Základ pro mocnění): ")
            n = inp(int, "Zadejte n (Modulo): ")
            ans = basics.discreteLogarithm.disLog(a, b, n)
            print("x = %d" % ans)
            input("Stiskněte enter pro pokračování.")

        elif option1 == 2:
            #GCD
            a = inp(int, "Zadejte první číslo: ")
            b = inp(int, "Zadejte druhé číslo: ")
            ans = basics.euklidesAlgorithm.euklides(a, b)
            print("Největší společný dělitel %d a %d je %d" % (a, b, ans))
            input("Stiskněte enter pro pokračování.")

    option = menu("Hlavní menu:", options)

    #^Zde bude hlavní logické jádro volající všechny potřebné funkce
#except ImportError:
 #   print("Nepodařilo se načíst důležité moduly")
