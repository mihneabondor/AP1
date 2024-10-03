def suma(n):
    s = 0
    while n:
        s += n
        n -= 1
    return s
print(suma(3))

def prim(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True
print(prim(7))

def cmmdc(a, b):
    while b:
        a, b = b, a % b
    return a
print(cmmdc(18, 3))