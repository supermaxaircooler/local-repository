import re

text1 = '11/27/2012 was the year of terror and chaos because of the future prophesied by movie 2012'
text2 = 'Nov 27, 2012'


altmethod = re.compile(r'(\d+)/(\d+)/(\d+)')

method = re.compile(r'\d+')
text = altmethod.match(text1)

print((text.group(0)))
print(text.group(1))
textmatch = method.findall(text1)
iterable = method.finditer(text1)
for m in iterable:
    print(m.group())