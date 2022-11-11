from collections import deque

N, M, K = map(int, input().split())
board = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue = deque()
mx_size = -1e9

for i in range(K):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 1

for i in range(N):
    for j in range(M):
        cnt = 0
        if board[i][j] == 1:
            cnt += 1
            visited[i][j] = True
            queue.append([i, j])

        while queue:
            y, x = queue.popleft()

            for direction in directions:
                ny = y + direction[0]
                nx = x + direction[1]

                if ny < 0 or ny >= N or nx < 0 or nx >= M:
                    continue
                if board[ny][nx] and not visited[ny][nx]:
                    cnt += 1
                    visited[ny][nx] = True
                    queue.append([ny, nx])

        mx_size = max(mx_size, cnt)

print(mx_size)
