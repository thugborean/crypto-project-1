import random

def rabinMiller(n) -> int:
    begin  = 2
    end = n - 2
    
    a = random.randInt(begin, end)




def calculateD(p,q,e) -> int:
    #d = e^-1 * (mod (p − 1)(q − 1))
    phi = ((p-1) * (q-1))
    val = pow(e,-1,phi)
    
    return val

def main():
    p = 7
    q = 11
    e = 13

    babbe = calculateD(p,q,e)
    print(babbe)

main()