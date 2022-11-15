N = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    start_x, start_y = map(int, input().split())

    for i in range(start_y, start_y + 10):
        for j in range(start_x, start_x + 10):
            board[i][j] = 1

area = 0
for i in range(101):
    for j in range(101):
        if board[i][j] == 1:
            area += 1

print(area)
