N = int(input())
board = [[0 for _ in range(1002)] for _ in range(1002)]

for n in range(1, N + 1):
    x, y, w, h = map(int, input().split())

    for i in range(y, y + h):
        for j in range(x, x + w):
            board[i][j] = n

ans = [0 for _ in range(101)]

for i in range(1002):
    for j in range(1002):
        if board[i][j] != 0:
            ans[board[i][j]] += 1

for i in range(1, N + 1):
    print(ans[i])