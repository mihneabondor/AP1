from math import sqrt


def prim(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def ex4(n):
    for i in range(2, n):
        if prim(i) & prim(n - i):
            return i, n - i
    return 0, 0

def ex5(n):
    n += 1
    while True:
        if prim(n) & prim(n + 2):
            return n, n + 2
        n += 1

def ex6(n):
    a = b = 1
    while b <= n:
        c = a + b
        a = b
        b = c
    return b

def ex7(n):
    p = 1
    for i in range(2, n//2+1):
        if n % i == 0:
            p *= i
    return p

def ex8(n):
    nr = [0]*10
    rez = 0
    while n:
        nr[n%10] += 1
        n //= 10
    for i in range(9, -1, -1):
        while nr[i]:
            rez = rez * 10 + i
            nr[i] -= 1
    return rez

def ex9(n):
    rez = 0
    while n:
        rez = rez * 10 + n % 10
        n //= 10
    return rez

def ex10(n):
    nr = [0]*10
    rez = 0
    while n:
        nr[n % 10] += 1
        n //= 10
    for i in range(1, 10):
        if nr[i]:
            rez = i
            nr[i] -= 1
            break
    for i in range(0, 10):
        while nr[i]:
            rez = rez * 10 + i
            nr[i] -= 1
    return rez


def ex11(a, b):
    nra = [0]*10
    nrb = [0]*10
    while a:
        nra[a % 10] += 1
        a //= 10
    while b:
        nrb[b % 10] += 1
        b //= 10
    for i in range(0, 10):
        if (nra[i] & nrb[i] == 0) | (nra[i] == 0 & nrb[i]):
            return False
    return True

def ex12(k):
    n = 1
    while True:
        div = 2
        cn = n
        while cn > 1:
            while cn % div == 0:
                cn //= div
                k -= 1
                if k == 0:
                    return div
            div += 1
        n += 1

def sumaDiv(n):
    sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum += i
    return sum

def ex14(n):
    while True:
        if n+1 == sumaDiv(n+1):
            return n + 1
        n += 1

def ex15(n):
    while n:
        if prim(n - 1) :
            return n - 1
        n -= 1
    print("Nu exista numar prim mai mic ca n")
    return 0

def ex16(n):
    while n:
        if n - 1 == sumaDiv(n - 1):
            return n - 1
        n -= 1
    print("Nu exista numar perfect mai mic n")
    return 0
