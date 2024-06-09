
x = 99
try:
    y = 1/0
except ZeroDivisionError as x: #python 3.x localizes the instance reference in except statement and removes the variable from memory completely
    print(x)

print(x)

# >>>  NameError 'x' is not defined