# ZADANIE11


def fibb(n):
    a, b = 0, 1
    for _ in range(int(n)):
        a, b = b, a + b
        yield a


ile = input("Ile chcesz wyrazow ciagu Fibonacciego: ")
n = fibb(ile)
for x in n:
    print(x)
