N = int(input())

board = []

for _ in range(N):
    row = []
    for _ in range(N):
        row.append(" ")
    board.append(row)


def solve(n, x, y):
    if n == 1:
        board[y][x] = "*"
        return

    n = int(n / 3)

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            solve(n, y + n * i, x + n * j)


solve(N, 0, 0)
for y in range(N):
    ans = ""
    for x in range(N):
        ans += board[y][x]
    print(ans)
