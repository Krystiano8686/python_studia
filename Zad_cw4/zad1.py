# ZADANIE1

zad1 = open("zad1.txt", "a+")
lista = []
for x in range(1, 101):
    if x % 4 == 0:
        lista.append(x)

print(lista)
zad1.write(str(lista))
zad1.close()
