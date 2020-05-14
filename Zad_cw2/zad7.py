# ZAD7

ilosc = int(input('Podaj ilosc liczby podnoszonych do kwadratu: '))
lista = []
for x in range(0, ilosc):
    a = int(input("Podaj liczę kótra zostanie podniesiona do kwadratu: "))
    a *= a
    lista.append(a)
print(f"Twoje liczby to: {lista}")
