
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
            #elif option == 2:
                #zašifrování
            option1 = menu("RSA", options1)
    #elif option == 2:
        #dh

    #elif option == 3:
        #basics

    option = menu("Hlavní menu:", options)

    #^Zde bude hlavní logické jádro volající všechny potřebné funkce
#except ImportError:
 #   print("Nepodařilo se načíst důležité moduly")
