# Zadanie 2

print("Podaj a i b")
a, b = float(input()), float(input())
print("Wybierz numer polecenia")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie bez reszty")
print("5. Dzielenie z resztą")
print("6. Potęgowanie")

polecenie = input()

if polecenie == "1":
    print("Wynik dodawania wynosi", a+b)
elif polecenie == "2":
    print("Wynik odejmowania wynosi", a-b)
elif polecenie == "3":
    print("Wynik mnożenia wynosi", a*b)
elif polecenie == "4":
    print("Wynik dzielenia wynosi", a/b)
elif polecenie == "5":
    print("Wynik dzielenia wynosi", a//b, "a reszta:", a % b)
elif polecenie == "6":
    print("Wynik potęgowania wynosi", a**b)
else:
    print("Nie ma polecenia o takim numerze")
