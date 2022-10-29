from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, sys.stdin.readline().split())
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

location = []
for k in range(1, K + 1):
    for i in range(N):
        for j in range(N):
            if board[i][j] == k:
                location.append([0, i, j])

queue = deque(location)
while queue:
    time, y, x = queue.popleft()

    if time == S:
        break

    for direction in directions:
        ny = y + direction[0]
        nx = x + direction[1]

        if ny < 0 or ny >= N or nx < 0 or nx >= N or board[ny][nx] != 0:
            continue

        if board[ny][nx] == 0:
            board[ny][nx] = board[y][x]
            queue.append([time + 1, ny, nx])

print(board[X - 1][Y - 1])
