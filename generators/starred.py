def f(a, b, c): print('%s, %s, and %s' % (a, b, c))

print(f(*range(3)))  #unpack range values
f(*(i for i in range(3))) # Unpack generator expression values