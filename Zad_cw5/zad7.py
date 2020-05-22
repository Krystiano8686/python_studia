# ZADANIE7


class ParzysteIndeksy:
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.end = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.end:
            raise StopIteration
        self.index = self.index + 1
        if self.index % 2 == 0:
            return self.data[self.index-1]
        else:
            return " "


def wyswietl(zdanie):
    result = ParzysteIndeksy(zdanie)
    while True:
        try:
            print(next(result), end="")
        except StopIteration:
            break
        print()


zdanie1 = "Nie rozumiem iteratorów"

wyswietl(zdanie1)
