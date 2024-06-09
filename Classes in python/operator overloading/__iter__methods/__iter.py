class Class:
    data = [2,3,"lode", "ka", "lassan"]
    def __init__(self):
        print("object created")
    # def __getitem__(self,index):
    #     return self.data[index]
    def __iter__(self):
        self.ite = iter(Class.data)
        return self.ite
    
    def __next__(self):
        return next(self.ite)
        

objec = Class()
objec1 = Class()

iterator1  = iter(objec)
iterator2 = iter(objec1)

for i in range(3):
    print(next(iterator1))

for i in range(2):
    print(next(iterator2))

# # for item in objec:                //iter method can be used
# #     print("item : ", item)

# try:
#     for i in range(8):                 #iter method can't be called
#         print("item  : ", objec[i])
# except IndexError:
#     print("problem resolved")

# for item in objec:
#     print(item)