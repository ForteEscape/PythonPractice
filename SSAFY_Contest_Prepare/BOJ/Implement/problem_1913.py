N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]

board[(N - 1) // 2][(N - 1) // 2] = 1
x, y = (N - 1) // 2, (N - 1) // 2
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

i = 2
start = 3
cnt_up, cnt_down, cnt_right, cnt_left = 0, 0, 0, 0

while x != 0 or y != 0:
    while i <= start ** 2:
        if x == y == (N - 1) // 2:
            cnt_up, cnt_down, cnt_right, cnt_left = start, start - 1, start - 2, start - 1
            x += dx[0]
            y += dy[0]
            cnt_up -= 1

        elif cnt_right > 0:
            x += dx[3]
            y += dy[3]
            cnt_right -= 1

        elif cnt_down > 0:
            x += dx[1]
            y += dy[1]
            cnt_down -= 1

        elif cnt_left > 0:
            x += dx[2]
            y += dy[2]
            cnt_left -= 1

        elif cnt_up > 0:
            x += dx[0]
            y += dy[0]
            cnt_up -= 1

        board[y][x] = i
        i += 1

    N -= 2
    start += 2

ans_y, ans_x = 0, 0
for row in range(len(board)):
    print(*board[row])
    for j in board[row]:
        if K in board[row]:
            ans_y = row + 1
            ans_x = board[row].index(K) + 1

print(ans_y, ans_x)