# ZADANIE6


class Wspak:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


zdanie1 = "Nie rozumiem iteratorów"
zdanie2 = "Fajne zdanie do testu"
zdanie1 = Wspak(zdanie1)
zdanie2 = Wspak(zdanie2)
for litera in zdanie1:
    print(litera)
for litera in zdanie2:
    print(litera)
