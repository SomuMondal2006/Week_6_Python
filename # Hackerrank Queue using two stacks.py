# Hackerrank: Queue using two stacks
# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem



def queue_using_two_stacks(queries):
    stack1 = []  
    stack2 = []  

    for query in queries:
        if query[0] == 1:
            stack1.append(query[1])

        elif query[0] == 2:
            if not stack2:
                while stack1:
                    stack2.append(stack1.pop())
            stack2.pop()

        elif query[0] == 3:
            if not stack2:
                while stack1:
                    stack2.append(stack1.pop())
            print(stack2[-1])


if __name__ == "__main__":
    q = int(input())  
    queries = []

    for _ in range(q):
        query = list(map(int, input().split()))
        queries.append(query)

    queue_using_two_stacks(queries)
