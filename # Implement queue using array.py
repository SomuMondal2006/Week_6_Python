# Implement queue using array
# https://www.geeksforgeeks.org/problems/implement-queue-using-array/1



class MyQueue:
    def __init__(self):
        self.queue = [] 
        self.front = 0  

    def push(self, x: int):
        self.queue.append(x)

    def pop(self):
        if self.front >= len(self.queue):
            return -1
        val = self.queue[self.front]
        self.front += 1
        return val


if __name__ == "__main__":
    queries = list(map(int, input().split()))

    q = MyQueue()
    i = 0

    while i < len(queries):
        if queries[i] == 1:
            q.push(queries[i + 1])
            i += 2
        elif queries[i] == 2:
            print(q.pop(), end=" ")
            i += 1
        else:
            i += 1
