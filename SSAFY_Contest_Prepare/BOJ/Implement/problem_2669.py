board = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    x2, y2 = x2 - 1, y2 - 1

    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            board[i][j] += 1

ans = 0
for i in range(1, 101):
    for j in range(1, 101):
        if board[i][j] != 0:
            ans += 1

print(ans)