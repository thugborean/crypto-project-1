import random

def rabinMiller(n) -> bool:
    # begin  = 2
    # end = n - 2
    # s = n - 1

    # a = random.randInt(begin, end)
    # x = pow(a,s,n)

    # if x == 1 or x == n - 1:
    #     return True 
    
    # for j = 1 to r = 1
    
    # step 1 - stop when m is not a while number
    k = 1
    m = 0
    newN = n - 1

    res = 0
    while True:
        res = newN / (2**k)
        if m == int(m):
            k += 1
            m = res
            continue
        else:
            break

    # step 2, 1 < a < n -1, we need a and m
    a = random.randint(1, newN)

    # b = a^m mod n
    b = pow(a, int(m), int(n))
    if b == 1 or b == -1:
        return True

    newB = pow(b, 2, int(n))
    if newB == 1:
        return False
    elif newB == -1:
        return True

    return False

def calculateD(p,q,e) -> int:
    # d = e^-1 * (mod (p − 1)(q − 1))
    phi = ((p-1) * (q-1))
    val = pow(e,-1,phi)
    
    return val

def main():
    p = 7
    q = 11
    e = 13

    babbe = calculateD(p,q,e)
    print(babbe)
    res = rabinMiller(1)
    print(res)

main()