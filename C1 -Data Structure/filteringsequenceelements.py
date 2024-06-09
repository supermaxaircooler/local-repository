mylist = [1, 4, -5,'NA', '-', 10, -7, 2, 3, -1]

def filter(val):
    try:
        x = int(val)
        return True
    
    except:
        return False

list = [n for n in mylist if filter(n)==1]

print(list)
