from collections import deque
import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(R)]

# visited = [[[0] * 2 for _ in range(C)] for _ in range(R)]
visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(2)]
visited[0][0][0] = 1
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

queue = deque()
queue.append([0, 0, 0])
ans = -1

while queue:
    z, y, x = queue.popleft()

    if y == R - 1 and x == C - 1:
        ans = visited[z][y][x]
        break

    for direction in directions:
        ny = y + direction[0]
        nx = x + direction[1]

        if 0 <= nx < C and 0 <= ny < R:
            if board[ny][nx] and z == 0:
                visited[1][ny][nx] = visited[0][y][x] + 1
                queue.append([1, ny, nx])
            elif not board[ny][nx] and not visited[z][ny][nx]:
                visited[z][ny][nx] = visited[z][y][x] + 1
                queue.append([z, ny, nx])
print(ans)
