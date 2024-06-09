from collections import deque
list = [2,4,2,"beta","male","sourav"]
de = deque(list, maxlen= 4)
print(de)
de.append("Kumar")
print(de.index("male",6,7))
#de.remove("beta")
print(de.count("sourav"))
#de.insert(2,2)
print(de)
print(type(de))

#deque(range(1,5))
#deque("abcd") = deque('a','b', 'c','d')
#de.remove("beta") :: remove first occurrence of "beta"
#del de[i] ::: remove item from i'th index