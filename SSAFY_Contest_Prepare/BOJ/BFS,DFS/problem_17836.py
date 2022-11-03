import copy
import sys
from collections import deque

N, M, T = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
board = [board, copy.deepcopy(board)]
queue = deque()
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]

queue.append([0, 0, 0])
visited[0][0][0] = True
ans = -1

while queue:
    sword, y, x = queue.popleft()

    if y == N - 1 and x == M - 1:
        ans = board[sword][y][x]
        break

    for direction in directions:
        ny = y + direction[0]
        nx = x + direction[1]

        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue

        if sword == 0 and not visited[sword][ny][nx] and board[sword][ny][nx] != 1:
            visited[sword][ny][nx] = True
            if board[sword][ny][nx] == 2:
                board[sword + 1][ny][nx] = board[sword][y][x] + 1
                visited[sword + 1][ny][nx] = True
                queue.append([sword + 1, ny, nx])
            else:
                board[sword][ny][nx] = board[sword][y][x] + 1
                queue.append([sword, ny, nx])
        elif sword == 1 and not visited[sword][ny][nx]:
            visited[sword][ny][nx] = True
            board[sword][ny][nx] = board[sword][y][x] + 1
            queue.append([sword, ny, nx])

if 0 < ans <= T:
    print(ans)
else:
    print("Fail")