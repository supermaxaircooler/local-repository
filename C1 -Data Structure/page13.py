dict1 = { 'anish': 2, 'prateek': 3, 'devashish': 4, 'puneet': 5}
dict2 = { 'kumar': 'anish' , 'jangra' : 'prateek', 'daima': "devashish", 'yadav': 'puneet'}


prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}
prices_and_names = list(zip(prices.values(), prices.keys()))
print(min(prices_and_names))
print(max(prices_and_names))  # no error because the zip file was saved to another variable