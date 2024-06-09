class Iterator:
    def __init__(self, start, stop):
        self.value = start -1
        self.stop = stop
        return None
    
    def __iter__(self):
        return self
    def __next__(self):
        if (self.value == self.stop):
            raise StopIteration
        self.value += 1
        return self.value**2

for item in Iterator(2,5):
    print(item, end =" : ")

# class Class:
#     data = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
