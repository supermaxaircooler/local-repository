from collections import defaultdict

d = defaultdict(list)
d['a'].append(2)
d['a'].append(5)
print(d)

'''
d['a'] = 2
d['a'].append(5)
 not working
'''