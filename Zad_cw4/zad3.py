# ZADANIE3

with open("zad3.txt", "w") as file:
    file.write("Pare \n")
    file.write("linijek \n")
    file.write("kodu")

with open("zad3.txt", "r") as file:
    for odczyt in file:
        print(odczyt)
