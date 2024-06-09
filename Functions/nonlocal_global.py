x = 88 # Global X

def lo():
    x = 40
    print(x)
    def func():
        x = 50
        print(x)
        def fn():
            nonlocal x
            x = 30
            print("fn x : {}".format(x))
        fn()

        
    func()
    print(" lo function x value is {}".format(x))
lo()
print(x)