
#^Místo pro základní Python moduly
#try:
from functionality.inp import inp
from functionality.menu import menu
import algorithms.rsa as rsa
from functionality.stopwatch import stopwatch
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
                input()
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
                        input()
                    elif option2 == 2:
                        #použít nové hodnoty
                        mod = inp(int, "Zadejte modulo kryptosystému:\n", "Zkuste to znovu:\n")
                        Pk = inp(int, "Zadejte veřejný klíč:\n", "Zkuste to znovu:\n")
                        mess = inp(int, "Zadejte číslo k zašifrování", "Zkuste to znovu")
                        encr = rsa.encrypt(mess, Pk, mod)
                        print("Zašifrované číslo je:\n%d" % encr)
                        input()
                else:
                    #použít nové hodnoty
                    mod = inp(int, "Zadejte modulo kryptosystému:\n", "Zkuste to znovu:\n")
                    Pk = inp(int, "Zadejte veřejný klíč:\n", "Zkuste to znovu:\n")
                    mess = inp(int, "Zadejte číslo k zašifrování", "Zkuste to znovu")
                    encr = rsa.encrypt(mess, Pk, mod)
                    print("Zašifrované číslo je:\n%d" % encr)
                    input()
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
                        input()
                
            option1 = menu("RSA", options1)
    #elif option == 2:
        #dh

    #elif option == 3:
        #basics

    option = menu("Hlavní menu:", options)

    #^Zde bude hlavní logické jádro volající všechny potřebné funkce
#except ImportError:
 #   print("Nepodařilo se načíst důležité moduly")
