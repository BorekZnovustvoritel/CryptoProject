from multiprocessing import Pool
from random import randint
from squareAndMultiply import squareAndMultiply
from primeGen import primeGen, primeFrom
from inverse import extendedEuklides as inverse
from primeTest import primeTest

def encrypt(num, publicKey, mod):
    return squareAndMultiply(num, publicKey, mod)

def decrypt(num, secretKey, mod):
    return squareAndMultiply(num, secretKey, mod)

def generate(bitLength = 2048, publicKey = None):
    if bitLength % 2 != 0:
        raise ValueError("Nelze vytvořit RSA o liché bitové délce.")
    primeBitLength = (bitLength // 2)
    with Pool(2) as p:
        r, s = p.map(primeGen, [primeBitLength, primeBitLength])
    mod = r * s
    #print(r, s)
    phiMod = (r - 1) * (s - 1)
    if (publicKey == None) or (primeTest(publicKey) == False):
        publicKey = primeFrom(3, phiMod - 2)
    secretKey = None
    while not secretKey:
        try:
            secretKey = inverse(publicKey, phiMod)
        except ValueError:
            secretKey = None
            continue
    return mod, publicKey, secretKey

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
                Pk = int(input("Zadejte veřejný klíč (Pokud necháte prázdné, vygeneruje se prvočíselný klíč):\n"))
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