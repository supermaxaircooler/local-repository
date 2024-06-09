def random(x):
    for i in range (x):
        yield 2*i**2

t1 = random(5)
t2 = iter(t1)
print(t1.__next__())
print(t1.__next__())

print(t2.__next__())
print(t1.__next__())
print(t2.__next__())