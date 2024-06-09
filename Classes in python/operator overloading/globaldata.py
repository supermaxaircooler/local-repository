class parent:
    data = [2,3,45,6,9]
    
x = parent()
y = parent()
x.data.append(34)
print(x.data)
print(parent.data)
print(y.data)