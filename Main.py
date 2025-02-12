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

def extendedGCD(a, b):
    if b == 0:
        return a, 1, 0  # Base case: gcd(a, 0) = a, coefficients (1, 0)
    
    gcd, x1, y1 = extendedGCD(b, a % b)  # Recursive call
    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y

def main():
    p = 7
    q = 11
    e = 13

    # res1 = calculateD(p,q,e)
    # print(res1)

    val = int(input("Input number to check if it's prime: "))
    res2 = rabinMiller(val, 20)
    print(res2)

    # res3 = inverseModM(1,4)
    # print(res3)

    # gcd, x, y = extendedGCD(27,46)
    # print(f"{gcd} + {x} + {y}")

main()

# def inverseModM(m, a):
#     # find v such that d = gcd(a,m) = a x v mod m, if d = 1 then v is the inverse of modulo m
#     v1 = 0
#     v2 = 1
#     d1 = m
#     d2 = a

#     while d2 != 0:
#         q = d1 / d2
#         t2 = v1 - q * v2
#         t3 = d1 - q * d2
#         v1 = v2
#         d1 = d2
#         v2 = t2
#         d2 = t3
    
#     v = v1
#     d = d1
#     if v < 0: v += m
#     # 0 < v < m
#     return v
