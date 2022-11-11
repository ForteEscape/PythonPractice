from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue = deque()
visited = [[False for _ in range(M)] for _ in range(N)]
is_percolates = False

for j in range(M):
    if board[0][j] == '0' and not visited[0][j]:
        visited[0][j] = True
        queue.append([0, j])

    while queue:
        y, x = queue.popleft()

        if y == N - 1:
            is_percolates = True
            break

        for direction in directions:
            ny = y + direction[0]
            nx = x + direction[1]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if board[ny][nx] == '0' and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append([ny, nx])

    if is_percolates:
        break

if is_percolates:
    print("YES")
else:
    print("NO")