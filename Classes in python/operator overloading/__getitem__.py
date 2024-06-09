class Class:
    data = [2,3,"lode", "ka", "lassan"]
    def __init__(self):
        print("object created")
    def __getitem__(self,index):
        return self.data[index]
    
    def __setitem__(self, indexfrom:int, value:list):
        for value in value:
            self.data[indexfrom] = value
            indexfrom+=1
    # def __setitem__(self,index,value):
    #     self.data[index] = value

chad = Class()

listvalue = ["this","is","corrected" ]

# chad[2,listvalue]
# print(chad.data)

chad[1]="st"
print(chad.data)

print(chad.__dict__)
