import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(y, x):
    visited = [[False for _ in range(M)] for _ in range(N)]
    distance = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    queue = deque()

    distance[y][x] = 1
    visited[y][x] = True
    queue.append([y, x])

    while queue:
        cy, cx = queue.popleft()

        for direction in directions:
            ny = cy + direction[0]
            nx = cx + direction[1]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if not visited[ny][nx] and board[ny][nx] == 'L':
                visited[ny][nx] = True
                distance[ny][nx] = distance[cy][cx] + 1
                cnt = max(cnt, distance[ny][nx])
                queue.append([ny, nx])

    return cnt - 1


result = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)
