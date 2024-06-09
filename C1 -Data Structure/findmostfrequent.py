'''
from collections import Counter

words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]

cal_count = Counter(words)
print(cal_count)
'''

'''

words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]

def fn(list):
    list2 = [0]*len(list)
    dict1 = dict(zip(list, list2))
    for items in list:
        dict1[items]+=1
    
    return dict1

print(fn(words))
        
'''
from collections import defaultdict

dd = defaultdict(str)

dd["default_key"] ="lawde"
dd['missingkey']
print(dd.items())
print(dd["key"])