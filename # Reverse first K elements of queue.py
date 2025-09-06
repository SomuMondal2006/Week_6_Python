# Reverse first K elements of queue
# https://www.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1



from collections import deque

def reverse_first_k_elements(q, k):
    if k > len(q):
        return list(q)

    stack = []

    for _ in range(k):
        stack.append(q.popleft())

    while stack:
        q.append(stack.pop())

    for _ in range(len(q) - k):
        q.append(q.popleft())

    return list(q)


q = deque([1, 2, 3, 4, 5])
k = 3
print(reverse_first_k_elements(q, k))  

q = deque([4, 3, 2, 1])
k = 4
print(reverse_first_k_elements(q, k)) 
