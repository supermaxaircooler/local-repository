

A = [2,3,5,5,6,6,10,50]

def rmv(list):
    seen = []
    for item in list:
        if item not in seen:
            seen.append(item)
            yield seen

list = rmv(A)
for i in list:
    print(list.__next__())
