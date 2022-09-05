import sys, copy

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
loc_cctv = []
board_simulate = []
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
mn = 1000001


# 카메라가 보는 곳을 모두 표시하는 함수
def look(x, y, direc):
    direc = direc % 4

    while True:
        x += directions[direc][1]
        y += directions[direc][0]

        if x < 0 or x >= m or y < 0 or y >= n or board_simulate[y][x] == 6:
            return
        if board_simulate[y][x] != 0:
            continue
        board_simulate[y][x] = 7


for i in range(n):
    for j in range(m):
        if 0 < board[i][j] < 6:
            loc_cctv.append([i, j])

# 카메라가 K개 있을 때 볼 수 있는 모든 조합은 4^K개가 된다
# 각 카메라는 4진법을 통하여 방향 전환이 가능하다
for tmp in range(1 << (2 * len(loc_cctv))):
    board_simulate = copy.deepcopy(board)

    brute = tmp
    for location in loc_cctv:
        direction = brute % 4
        brute = brute // 4

        cctv_y = location[0]
        cctv_x = location[1]

        if board[cctv_y][cctv_x] == 1:
            look(cctv_x, cctv_y, direction)
        elif board[cctv_y][cctv_x] == 2:
            look(cctv_x, cctv_y, direction)
            look(cctv_x, cctv_y, direction + 2)
        elif board[cctv_y][cctv_x] == 3:
            look(cctv_x, cctv_y, direction)
            look(cctv_x, cctv_y, direction + 1)
        elif board[cctv_y][cctv_x] == 4:
            look(cctv_x, cctv_y, direction)
            look(cctv_x, cctv_y, direction + 1)
            look(cctv_x, cctv_y, direction + 2)
        elif board[cctv_y][cctv_x] == 5:
            look(cctv_x, cctv_y, direction)
            look(cctv_x, cctv_y, direction + 1)
            look(cctv_x, cctv_y, direction + 2)
            look(cctv_x, cctv_y, direction + 3)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if board_simulate[i][j] == 0:
                cnt += 1

    if cnt < mn:
        mn = cnt

print(mn)