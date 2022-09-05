import sys

N, M, dice_y, dice_x, k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cmd = list(map(int, sys.stdin.readline().split()))
dice = [[0] * 3 for _ in range(4)]
directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]


for i in range(len(cmd)):
    ny = dice_y + directions[cmd[i] - 1][0]
    nx = dice_x + directions[cmd[i] - 1][1]

    if ny < 0 or ny >= N or nx < 0 or nx >= M:
        continue

    dice_y = ny
    dice_x = nx

    if cmd[i] == 3:
        temp = dice[0][1]
        for j in range(3):
            dice[j][1] = dice[j + 1][1]

        dice[3][1] = temp
    elif cmd[i] == 4:
        temp = dice[3][1]
        for j in range(1, 4):
            dice[4-j][1] = dice[4-1-j][1]

        dice[0][1] = temp
    elif cmd[i] == 1:
        temp = dice[1][2]
        for j in range(1, 3):
            dice[1][3-j] = dice[1][3-1-j]

        dice[1][0] = temp

        temp = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = temp
    elif cmd[i] == 2:
        temp = dice[1][0]
        for j in range(2):
            dice[1][j] = dice[1][j + 1]
        dice[1][2] = temp

        temp = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = temp

    print(dice[1][1])

    if board[dice_y][dice_x] == 0:
        board[dice_y][dice_x] = dice[3][1]
    else:
        dice[3][1] = board[dice_y][dice_x]
        board[dice_y][dice_x] = 0


