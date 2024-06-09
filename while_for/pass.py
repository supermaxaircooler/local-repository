def fn():
    pass

def fn2():
    ...                         #alternate to pass which means do nothing, used in defining empty functions or for later to be filled in

def fn3(x):
    print("lode ki sarkar {}".format(x))

if __name__ == "__main__":
    x = int(input("lode ki sarkar"))
    fn3(x)