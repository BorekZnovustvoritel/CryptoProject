from time import perf_counter
from rsa import generate
from eulerPhi import phi

def stopwatch(foo, **kwargs):
    ref = perf_counter()
    ans = foo(**kwargs)
    stop = perf_counter() - ref
    return ans, stop

if __name__ == "__main__":
    ans, stop = stopwatch(generate)#, bitLength = 512)#, publicKey = 7)
    mod, Pk, Sk = ans
    print("Mod = %d\nPk = %d\nSk = %d\n\nThis process took %.2f seconds." % (mod, Pk, Sk, stop))
    #phi, time = stopWatch(phi, num = 19)
    #print(phi, time)
