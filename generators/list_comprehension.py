obj = (x**3 for x in range(7))

# print(list(obj))
try:
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())

except StopIteration:
    print("out of storage")


obj.close()

print(obj.__next__())
