import heapq

class priorityqueue:
    index = 0
    def __init__(self):
        self.queue = []
    def push(self, x , priority):
        heapq.heappush(self.queue , (x, priority))
    def pop(self):
        return print(heapq.heappop(self.queue)[0])

def main():
    p = priorityqueue()
    p.push("mahesh", 1)
    p.push("dalle", 5)
    p.push("ash", 3)
    p.push("pus", 2)
    p.pop()
    p.pop()
    return 0

if __name__ == "__main__":
    main()


