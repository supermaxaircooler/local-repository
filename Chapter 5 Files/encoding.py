import sys
print(sys.getdefaultencoding())
with open("Chapter 5 Files/testing.txt", encoding = 'latin-1', newline ='') as f:
    f.read()