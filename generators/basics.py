def random(x):
    for i in range (x):
        yield i**2


test = random(5)
for x in random(6):
    print(x, end = " ")


