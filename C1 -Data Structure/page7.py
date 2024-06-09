import heapq
list_= [3,5,2,5,7,8,11,15]
heapq.heapify(list_)
print(list_)
heapq.heappop(list_)
print(list_)
heapq.heappush(list_, -4)
print(list_)
heapq.heapreplace(list_, 1)   #first pops then pushes
print(list_)
heapq.heappushpop(list_ , 0)   #first pushes then pops
print(list_)

#assignment operator doesnt work on heapq 