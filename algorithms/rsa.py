#from multiprocessing import Pool
from random import randint
from basics.squareAndMultiply import squareAndMultiply
from basics.primeGen import primeGen
from basics.inverse import extendedEuklides as inverse
from basics.primeTest import primeTest

def encrypt(num, publicKey, mod):
    return squareAndMultiply(num, publicKey, mod)

def decrypt(num, privateKey, mod):
    return squareAndMultiply(num, privateKey, mod)

def generate(bitLength = None, publicKey = None):
    if not bitLength:
        bitLength = 2048
    if bitLength % 2 != 0:
        raise ValueError("Nelze vytvořit RSA o liché bitové délce.")
    primeBitLength = (bitLength // 2)
    print("Generuji prvočísla o délce %d bitů..." % primeBitLength)
    r = primeGen(primeBitLength)
    print("1/2 hotovo!")
    s = primeGen(primeBitLength)
    #with Pool(2) as p:
    #    r = p.apply_async(primeGen, (primeBitLength,)).get()
    #    s = p.apply_async(primeGen, (primeBitLength,)).get()
    #    r, s = p.map(primeGen, [primeBitLength, primeBitLength])
    #    p.join()
    mod = r * s
    print("Hotovo!")
    phiMod = (r - 1) * (s - 1)
    print("Generuji klíče...")
    if (publicKey == None):
        publicKey = randint(3, phiMod - 2)
    privateKey = None
    while not privateKey:
        try:
            privateKey = inverse(publicKey, phiMod)
        except ValueError:
            publicKey = randint(3, phiMod - 2)
            continue
    return mod, publicKey, privateKey

if __name__ == "__main__":
    exit = False
    while not exit:
        alg = int(input("\n\nZadejte:\n1) pro sestavení RSA\n2) pro zašifrování\n3) pro dešifrování\n4) pro ukončení\n"))
        if alg == 1:
            try:
                bitLength = int(input("Zadejte bitovou délku modula veřejného klíče (Pokud necháte prázdné, nastaví se 2048):\n"))
            except ValueError:
                bitLength = 2048
            try:
                Pk = int(input("Zadejte veřejný klíč (Pokud necháte prázdné, vygeneruje se náhodný klíč):\n"))
            except ValueError:
                Pk = None
            mod, Pk, Sk = generate(bitLength, Pk)
            print("\nmod = %d\nPk = %d\nSk = %d" % (mod, Pk, Sk))
        elif alg == 2:
            num = int(input("Zadejte číslo k zašifrování:\n"))
            Pk = int(input("Zadejte veřejný klíč:\n"))
            mod = int(input("Zadejte modulo:\n"))
            print("\nZašifrovaná zpráva je: "+str(encrypt(num, Pk, mod)))
        elif alg == 3:
            num = int(input("Zadejte číslo k dešifrování:\n"))
            Pk = int(input("Zadejte soukromý klíč:\n"))
            mod = int(input("Zadejte modulo:\n"))
            print("\nDešifrovaná zpráva je: "+str(encrypt(num, Pk, mod)))
        elif alg == 4:
            exit = True