from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
directions = [[1, 0], [1, 1], [1, -1], [-1, 0], [-1, 1], [-1, -1], [0, 1], [0, -1]]

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            queue.append([i, j])

while queue:
    y, x = queue.popleft()

    for direction in directions:
        ny = y + direction[0]
        nx = x + direction[1]

        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if board[ny][nx] == 0:
            board[ny][nx] = board[y][x] + 1
            queue.append([ny, nx])

ans = -1e9
for i in range(N):
    for j in range(M):
        ans = max(ans, board[i][j])

print(ans - 1)