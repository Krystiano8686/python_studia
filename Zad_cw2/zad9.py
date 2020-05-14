# ZAD9

liczba = int(input('Podaj liczbę wielocyfrową: '))

suma = 0
while liczba != 0:
    suma += liczba % 10
    liczba //= 10
print(suma)
