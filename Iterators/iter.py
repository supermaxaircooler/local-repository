list = [2,3,4,5,10]
ite = list.__iter__()
print(ite.__next__(),  sep = ',', end =" ")
print(ite.__next__(), sep=",",end = " ")
print(ite.__next__(), sep = ",",end = " ")
print(ite.__next__())
print(ite.__next__(), end = " ")
print(next(ite))
