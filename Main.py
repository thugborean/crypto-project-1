import random
import time

def generatePrimes(numbersToGenerate, sizeOfNumbersInBits, iterations) -> set[int]:
    # start the clock
    startTime = time.time()

    listOfPrimes = set()
    while len(listOfPrimes) < numbersToGenerate:
        number = random.getrandbits(sizeOfNumbersInBits)
        # check if the random number is a prime
        isPrime = rabinMiller(number, iterations)
        if isPrime: listOfPrimes.add(number)
    
    # end the clock
    endTime = time.time()
    print(f"Time elapsed: {endTime - startTime} seconds, to generate {numbersToGenerate} primes of size {sizeOfNumbersInBits} bits")

    return listOfPrimes

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
        x = pow(a, m, n)
        if x == 1 or x == n - 1:
            continue

        isComposite = True
        for j in range(k - 1):
            x = pow(x, 2, n)  # x = x^2 % n
            if x == n - 1:
                isComposite = False
                break

        if isComposite:
            return False

    return True

def calculateD(p,q,e) -> int:
    # d = e^-1 * (mod (p − 1)(q − 1))
    phi = ((p-1) * (q-1))
    val = pow(e,-1,phi)
    
    return val

def extendedGCD(a, b) -> tuple [int, int, int]:
    if b == 0:
        return a, 1, 0  # gcd(a, 0) = a, and x = 1, y = 0
    
    gcd, x1, y1 = extendedGCD(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y

def main():

    while True:
        # generate primes
        gen = generatePrimes(3, 512, 20);
        listOfPrimes = list(gen)
        # p
        p = listOfPrimes[0]
        # q
        q = listOfPrimes[1]
        # e
        e = 2**16 + 1
        # m
        m = (p-1) * (q-1)
        # N
        N = p * q
        s = listOfPrimes[2]
        c = pow(s,e,N)

        choice = input("Choose option: \n(1) Generate Primes\n(2) Perform extended GCD\n(3) Calculate D\n(4) Exit \n")
        try:
            choice = int(choice)
            if (choice < 1 and choice > 5):
                print("Invalid choice!")
                continue
        except:
            print("Invalid choice!")
            continue

        if choice == 1:
            numberOfPrimes = input("Enter number of primes to generate: ")
            sizeOfNumbersInBits = input("Enter size of primes in bits: ")
            try:
                numberOfPrimes = int(numberOfPrimes)
                sizeOfNumbersInBits = int(sizeOfNumbersInBits)
            except:
                print("Invalid Input/s!")
                continue
            listOfPrimes = generatePrimes(numberOfPrimes, sizeOfNumbersInBits, 20)
            for prime in listOfPrimes:
                print(prime)
        elif choice == 2:
            gcd, x, y = extendedGCD(p,q)
            print(f"{gcd} + {x} + {y}")
        elif choice == 3:
            d = calculateD(p, q, e)
            if (e * d % m == 1):
                print(f"D is: {d}")
                print("The algorithm works!")

            z = pow(c, d, N)
            print(f"Z is: {z}!")
        elif choice == 4: break
    
    print("Program exiting!")

if __name__ == "__main__":
    main()