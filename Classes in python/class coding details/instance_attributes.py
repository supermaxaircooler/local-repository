import math as m
class database:
    data = 16
    data = m.sqrt(data)
    def printsomething():
        return print("hello world", database.data)
    
    def __init__(self, data):
        self.data = data
    def setvalue(self, age):
        self.age = age
    
    def getvalue(self):
        return print(self.age)



ob  = database("stree")
ob.setvalue(23)
print(ob.getvalue(), database.data)