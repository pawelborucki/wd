class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
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
kol1 = Wspak("Stefan")
for i in range(kol1.index):
    print(kol1.__next__())
kol2 = Wspak("Maciuś")
for x in range(kol2.index):
    print(kol2.__next__())