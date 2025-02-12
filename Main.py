import random

def rabinMiller(n, iterations) -> bool:
    # step 0, quick check
    if n == 1 or n == 2 or n == 3: return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0: return False

    # step 1, stop when m is not a whole number
    newN = n - 1
    k = 1    #r
    m = newN #s

    res = 0
    while True:
        res = newN / (2**k)

        # check for decimal
        if res % 1 != 0:  
            break
        
        k += 1
        m = res

    # step 2, 1 < a < n -1, we need a and m
    a = random.randint(2, n - 2)

    # step 3, x = a^m mod n
    for i in range(iterations):
        x = pow(a, int(m), int(n))
        if x == 1 or x == n - 1:
            continue

        is_composite = True
        for j in range(k - 1):
            x = pow(x, 2, n)  # x = x^2 % n, dubblar exponenten varje gång vi testar
            if x == n - 1:
                is_composite = False
                break

        if is_composite:
            return False  # Hittade en witness

    return True


def calculateD(p,q,e) -> int:
    # d = e^-1 * (mod (p − 1)(q − 1))
    phi = ((p-1) * (q-1))
    val = pow(e,-1,phi)
    
    return val

def main():
    p = 7
    q = 11
    e = 13

    # res1 = calculateD(p,q,e)
    # print(res1)

    val = int(input("Input number to check if it's prime: "))
    res2 = rabinMiller(val, 20)
    print(res2)

main()