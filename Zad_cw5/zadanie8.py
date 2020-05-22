# ZADANIE8


class Samogloski:

    def __init__(self, zdanie):
        if isinstance(zdanie, str):
            self.zdanie = zdanie
        else:
            raise TypeError
        self.index = 0
        self.end = len(zdanie)+1

    def __iter__(self):
        return self

    def __next__(self):
        samogłoski = ["a", "ą", "e", "ę", "i", "o", "ó", "u", "y"]
        while self.zdanie[self.index].lower() not in samogłoski:
            self.index += 1
        buffer = self.zdanie[self.index]
        self.index += 1
        return buffer


def wyswietl(zdanie):
    result = Samogloski(zdanie)
    while True:
        try:
            print(next(result), end="")
        except StopIteration:
            break
        print()


zdanie1 = "Oddaj mi tylko same samogłoski"

wyswietl(zdanie1)
