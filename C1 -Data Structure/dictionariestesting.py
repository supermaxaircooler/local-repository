x = {'c': 5,
     'a' : 3,
     'b': 10
     }

print(type(x.values()))
print(type(x.items()))
'''
x.pop('c')
for keys, values in x.items():
    print(keys, " : ",values)

x.update({'c' : 11})
for keys, values in x.items():
    print(keys, " : ", values)


#del x['b']

for keys, values in x.items():
    print(keys, " : ", values)

'''