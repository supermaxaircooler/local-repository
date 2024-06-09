from collections import defaultdict
from operator import itemgetter
class sort:
    dict1 = defaultdict(list)
    def __init__(self, uname, uid):
        self.uname = uname
        self.uid = uid
        self.dict1[uname] = uid

    
    def return_uid(self):
        return self.uid
    
    def __call__(self):
        print(f"{self.uid} :  {self.uname}")
        return 0

obj = [sort("anish", 10005),
    sort("prateek", 10002),
    sort("Devashish", 1001)]

list = sorted(obj, key = lambda x : x())


def printf(list):
    for item in list:
        yield item()

sortedarray = printf(list)

for item in list:
    sortedarray.__next__()


#list = sorted(sort.dict1.items(), key = itemgetter(1))
print(list)