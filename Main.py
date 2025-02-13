import random
import time

def generatePrimes(numbersToGenerate, sizeOfNumbersInBits, iterations):
    startTime = time.time()

    listOfPrimes = set()
    while len(listOfPrimes) < numbersToGenerate:
        number = random.getrandbits(sizeOfNumbersInBits)
        # check it the random number is a prime
        isPrime = rabinMiller(number, iterations)
        if isPrime: listOfPrimes.add(number)
    
    endTime = time.time()
    print(f"Time elapsed: {endTime - startTime} seconds, to generate {numbersToGenerate} primes of size {sizeOfNumbersInBits}")

def rabinMiller(n, iterations) -> bool:
    # step 0, quick check
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False


    # step 1, stop when m is not a whole number
    newN = n - 1
    k = 1    #r
    m = newN #s

    # Factor n-1 as (2^k)*m
    m = n - 1
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1

    # step 2, x = a^m mod n
    for i in range(iterations):
        a = random.randint(2, n - 2)
        x = pow(a, int(m), int(n))
        if x == 1 or x == n - 1:
            continue

        isComposite = True
        for j in range(k - 1):
            x = pow(x, 2, n)  # x = x^2 % n, dubblar exponenten varje gång vi testar
            if x == n - 1:
                isComposite = False
                break

        if isComposite:
            return False  # Hittade en witness

    return True

def calculateD(p,q,e) -> int:
    # d = e^-1 * (mod (p − 1)(q − 1))
    phi = ((p-1) * (q-1))
    val = pow(e,-1,phi)
    
    return val

def extendedGCD(a, b) -> int:
    if b == 0:
        return a, 1, 0  # Base case: gcd(a, 0) = a, coefficients (1, 0)
    
    gcd, x1, y1 = extendedGCD(b, a % b)  # Recursive call
    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y

def main():
    # p
    a = 5411871029092462825516185209329155738882437723668937447678705813383753989896625756765214367131469274835377472645480091140402399461250152678125693930035771
    # q
    m = 9714555070505236732818155692536136618594137166972361243648893311925812214088974952419769198868507372533717366520228097147768109020620023156613694426379779
    e = 2**16 + 1
    # e * d / (mod (a - 1)(m - 1)) = 1
    gcd, x, y = extendedGCD(a,m)
    print(f"{gcd} + {x} + {y}")


    inverse = True
    if (gcd != 1): inverse = False
    print(inverse)

    # res = calculateD(p,q,e)
    # print(res1)

    # listOfPrimes = set()
    # while len(listOfPrimes) < 100:
    #     number = random.getrandbits(4096)
    #     isPrime = rabinMiller(number, 20)
    #     if isPrime: listOfPrimes.add(number)
        
    # res3 = inverseModM(1,4)
    # print(res3)
main()