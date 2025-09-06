# Interleave halves of queue
# https://www.geeksforgeeks.org/problems/interleave-the-first-half-of-the-queue-with-second-half/1



from collections import deque

def interleave_queue(q):
    n = len(q)

    if n % 2 != 0:
        return list(q)
    
    mid = n // 2

    first_half = deque([q[i] for i in range(mid)])
    second_half = deque([q[i] for i in range(mid, n)])
    
    result = deque()
    
    while first_half and second_half:
        result.append(first_half.popleft())  
        result.append(second_half.popleft()) 
    
    return list(result)

q = [2, 4, 3, 1]
print(interleave_queue(q)) 

q = [3, 5]
print(interleave_queue(q))  
