# Implement queue using linked list
# https://www.geeksforgeeks.org/problems/implement-queue-using-linked-list/1



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def push(self, x):
        new_node = Node(x)
        if self.rear is None: 
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def pop(self):
        if self.front is None: 
            return -1
        popped_value = self.front.data
        self.front = self.front.next
        if self.front is None: 
            self.rear = None
        return popped_value

if __name__ == "__main__":
    Q = int(input("Enter number of queries: "))
    queries = []

    for _ in range(Q):
        q = list(map(int, input().split()))
        queries.append(q)

    q = Queue()  
    output = []

    for query in queries:
        if query[0] == 1:
            q.push(query[1])
        elif query[0] == 2:
            output.append(q.pop())

    print(*output)
