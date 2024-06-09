def fn(x):
    try:
        for i in range (x):
            y = yield x%3
            if y =="break":
                break
            else:
                print("try again")
    except (GeneratorExit, StopIteration):
        print("geneartor is existing")
    

obj = fn(10)
obj.__next__()
obj.send("nice try")
print(obj.send("lol"))
obj.send("break")



