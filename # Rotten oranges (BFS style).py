# Rotten oranges (BFS style)
# https://www.geeksforgeeks.org/problems/rotten-oranges2536/1



from collections import deque

def minTimeToRotAllOranges(mat):
    if not mat or not mat[0]:
        return -1

    n, m = len(mat), len(mat[0])
    queue = deque()
    fresh = 0

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 2:
                queue.append((i, j, 0)) 
            elif mat[i][j] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    time = 0
    rotten_count = 0

    while queue:
        x, y, t = queue.popleft()
        time = max(time, t)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1:
                mat[nx][ny] = 2  
                queue.append((nx, ny, t + 1))
                rotten_count += 1

    return time if rotten_count == fresh else -1

if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    m = int(input("Enter number of columns: "))

    mat = []
    print("Enter the matrix values row-wise (0, 1, 2):")
    for _ in range(n):
        row = list(map(int, input().split()))
        mat.append(row)

    result = minTimeToRotAllOranges(mat)

    print("Minimum time to rot all oranges:", result)
