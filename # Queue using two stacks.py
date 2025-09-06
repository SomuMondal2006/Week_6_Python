# Queue using two stacks
# https://www.geeksforgeeks.org/problems/queue-using-two-stacks/1



class QueueUsingStacks:
    def __init__(self):
        self.s1 = []  
        self.s2 = []  

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        if not self.s2:
            return -1
        
        return self.s2.pop()


def process_queries(q, queries):
    queue = QueueUsingStacks()
    result = []

    for query in queries:
        if query[0] == 1:  
            queue.push(query[1])
        elif query[0] == 2:  
            result.append(queue.pop())

    return result


q = 5
queries = [[1, 2], [1, 3], [2], [1, 4], [2]]
print("Output:", process_queries(q, queries))  

q = 4
queries = [[1, 2], [2], [2], [1, 4]]
print("Output:", process_queries(q, queries))  
