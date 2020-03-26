print("Hello world")  # wersja 3.x
# print"Hello world"   # wersja 2.x

# C#, C++, Java, PHP

# def main():
#     for elem in kolekcja:
#         if costam <0:

imie = "Ala"
imie = 0
imie = None

# łańcuchy znaków
imie = "Ala"
print(type(imie))
imie = str("Ala")
# imie = str(100) #"100"

# imie[0] ="O" # nie jest mutowalny
imie = imie.lower()
print(imie)

# typy liczbowe
liczba = 1
liczbaf = 4.5

print(type(liczba))
print(type(liczbaf))

print(0.1 + 0.2 == 0.3)
print(f"{0.1:.32f}")
print(f"{0.2:.32f}")
print(f"{0.3:.32f}")  # od wersji 3.6

print("Ala" + " ma kota")
print("Ala" + " ma " + str(5) + " kotów")
print("Ala ma {1}{0} kotów".format(5, 4))
# f-string
ilosc_kotow = 5
print(f"Ala ma {ilosc_kotow} kotów")
# print(f"{"Ala":>10}") #pyformat.info

# Decimal lub zaokrąglanie

liczba = "100"
print(int(liczba))
print(int(liczba, 2))
