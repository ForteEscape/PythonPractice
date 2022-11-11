from collections import deque

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
start_y, start_x, end_y, end_x = map(int, input().split())
board[start_y][start_x] = 1
directions = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]
queue = deque()
queue.append([start_y, start_x])

while queue:
    y, x = queue.popleft()

    if y == end_y and x == end_x:
        print(board[y][x] - 1)
        break

    for direction in directions:
        ny = y + direction[0]
        nx = x + direction[1]

        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if not board[ny][nx]:
            board[ny][nx] = board[y][x] + 1
            queue.append([ny, nx])

if not board[end_y][end_x]:
    print(-1)