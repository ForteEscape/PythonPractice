import sys, copy
from itertools import combinations
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
virus = []
unreachable_cnt = 0
sec = []
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
final_y, final_x = 0, 0
cnt = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append([i, j])
            board[i][j] = 0
        elif board[i][j] == 1:
            board[i][j] = -1

combs = list(combinations(virus, m))

for comb in combs:
    cnt += 1
    queue = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    board2 = copy.deepcopy(board)

    for c in comb:
        y, x = c
        board2[y][x] = 1
        visited[y][x] = True
        queue.append(c)

    while queue:
        y, x = queue.popleft()
        final_y, final_x = y, x

        for direction in directions:
            ny = y + direction[0]
            nx = x + direction[1]

            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and board[ny][nx] != -1:
                visited[ny][nx] = True
                board2[ny][nx] = board2[y][x] + 1
                queue.append([ny, nx])

    flag = False
    for i in range(n):
        for j in range(n):
            if board2[i][j] == 0:
                unreachable_cnt += 1
                flag = True
                break
        if flag:
            break
    if not flag:
        sec.append(board2[final_y][final_x] - 1)

if cnt == unreachable_cnt:
    print("-1")
else:
    print(min(sec))


