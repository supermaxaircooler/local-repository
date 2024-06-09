class class1:
    iter3 = 3       # is not recognized inside functions
    def fn(self, name):
        self.name = name
    def getfn(self):
        return self.name, self.roll , self.desg
    
    def __init__(self, roll, desg):
        self.roll = roll
        self.desg = desg

class childclass(class1):
    pass


# obj = class1()

# class1.fn(obj, "lode")
# print(class1.getfn(obj))

obj = childclass(*["21103015", "student"])
obj.fn("lode")
for i in obj.getfn():
    print(i, "string", sep= " : " , end = " ")
