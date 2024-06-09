with open('Chapter 5 Files/testing.txt', 'rt') as f:
        object = \
                f.readlines()
        for line in object:
                print(line, end ='')