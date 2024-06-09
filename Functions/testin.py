l = [3,4,5]
tup = ("lode", "ki", "sarkar")

def fn(arg1, *,arg2, arg3):
    return (arg1+arg2+arg3)


def fn2():
    pass
print(fn(arg3 = 10, arg2 = 10, arg1=15))