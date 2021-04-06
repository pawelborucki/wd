class Parzyste:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        yield self

    def __next__(self):
        if len(self.data) - 1 < self.index:
            raise StopIteration
        text = self.data[self.index]
        self.index += 2
        yield text
kol1 = Parzyste("stefan")
print(next(kol1))

    