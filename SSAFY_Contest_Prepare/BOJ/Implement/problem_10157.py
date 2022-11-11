N, M = map(int, input().split())
location = int(input())
board = [[0 for _ in range(M)] for _ in range(N)]

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
direction = y = x = 0

if location > N * M:
    print(0)
    exit(0)

for i in range(1, N * M + 1):
    if i == location:
        print(y + 1, x + 1)
        break
    else:
        board[y][x] = i
        y += directions[direction][0]
        x += directions[direction][1]

        if x < 0 or y < 0 or x >= M or y >= N or board[y][x]:
            x -= directions[direction][1]
            y -= directions[direction][0]

            direction = (direction + 1) % 4

            y += directions[direction][0]
            x += directions[direction][1]
