import sys
# print(sys.path)
pack_pth = r"C:\\Users\Anish Kumar\\Pictures\\Machine Learning\\Python\\programs.py"
sys.path.extend(pack_pth)

# import package

# package.fn(23, [23,45,5])
import notting

print(notting.add1.addofcubes(2,3))

list =[]
for x in notting.cstmpackage.fn(10):
    list.append(x)

print(list, sep=" :: ")