import heapq

rows = [
 {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
 {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
 {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
 {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

list = heapq.nlargest(len(rows), rows, key = lambda x : x["uid"])
print(list)