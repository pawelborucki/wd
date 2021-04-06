class Samogloski:
    def __init__(self, data):
        if isinstance(data, str):
            self.data = data
        else:
            return "To nie jest string"
    def __iter__(self):
        return self
    def __next__(self):
        data2 = []
        samo = ["a", "e", "i", "o", "u", "y"]
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if(self.data[i] == samo[j]):
                    data2.append(self.data[i]) 
        return data2

kol1 = Samogloski("Stefan")
print(kol1.__next__())

