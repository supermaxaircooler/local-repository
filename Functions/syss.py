import sys
print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)

print(dir(sys.getrecursionlimit), end ="\n\n")
print(dir(sys.getrecursionlimit.__call__))
# print(sys.getrecursionlimit.__name__)
# print(sys.getrecursionlimit.__code__.__class__)