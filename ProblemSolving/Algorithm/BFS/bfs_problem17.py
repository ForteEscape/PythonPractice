from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
t = 0
tmp = 0

cnt_cheese = 0
for i in range(1, N):
    for j in range(1, M):
        if board[i][j] == 1:
            cnt_cheese += 1

while cnt_cheese != 0:
    tmp = cnt_cheese
    queue = deque()
    destroy_location = deque()
    visit = [[False for _ in range(M)] for _ in range(N)]

    visit[0][0] = True
    queue.append([0, 0])

    while queue:
        y, x = queue.popleft()

        for direction in directions:
            ny = y + direction[0]
            nx = x + direction[1]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if board[ny][nx] == 0 and not visit[ny][nx]:
                visit[ny][nx] = True
                queue.append([ny, nx])
            elif board[ny][nx] == 1 and not visit[ny][nx]:
                visit[ny][nx] = True
                destroy_location.append([ny, nx])

    while destroy_location:
        y, x = destroy_location.popleft()
        board[y][x] = 0

    t += 1

    cnt_cheese = 0
    for i in range(1, N):
        for j in range(1, M):
            if board[i][j] == 1:
                cnt_cheese += 1

print(t)
print(tmp)
