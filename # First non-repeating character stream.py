# First non-repeating character stream
# https://www.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream/1



from collections import deque

def first_non_repeating(s):
    freq = {}
    q = deque()
    result = []

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
        q.append(ch)

        while q and freq[q[0]] > 1:
            q.popleft()

        if q:
            result.append(q[0])
        else:
            result.append('#')

    return "".join(result)


s = "aabc"
print(first_non_repeating(s)) 

s = "zz"
print(first_non_repeating(s)) 

s = "bb"
print(first_non_repeating(s)) 
