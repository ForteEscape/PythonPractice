import sys

n, m = map(int, sys.stdin.readline().split())
cy, cx, d = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
cnt = 0
cleaned_cnt = 0

while True:
    # cleaning
    visited[cy][cx] = True

    if cnt == 4:
        ny = cy - directions[d][0]
        nx = cx - directions[d][1]

        if board[ny][nx] == 1:
            break
        else:
            cy, cx = ny, nx
            cnt = 0
            continue

    tmp = d
    tmp -= 1
    if tmp < 0:
        tmp = 3

    ny = cy + directions[tmp][0]
    nx = cx + directions[tmp][1]

    if board[ny][nx] != 1 and not visited[ny][nx]:
        d = tmp
        cy, cx = ny, nx
        cnt = 0
        continue
    else:
        d = tmp
        cnt += 1
        continue


for i in range(n):
    for j in range(m):
        if visited[i][j]:
            cleaned_cnt += 1

print(cleaned_cnt)



