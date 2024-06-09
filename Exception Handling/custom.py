class class1:
    iter3 = 3       # is not recognized inside functions
    def fn(self, name):
        self.name = name
    def getfn(self):
        return self.name, self.roll , self.desg
    

raise class1 as obj
