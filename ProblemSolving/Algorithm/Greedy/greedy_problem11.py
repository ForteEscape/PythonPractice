import sys

N, M = map(int, sys.stdin.readline().split())
board_original = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
board_result = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
cnt = 0


def flip(y, x):
    for i in range(y, y + 3):
        for j in range(x, x + 3):
            if board_original[i][j] == '1':
                board_original[i][j] = '0'
            else:
                board_original[i][j] = '1'
    return


def chk():
    for i in range(N):
        for j in range(M):
            if board_original[i][j] != board_result[i][j]:
                return False

    return True


for i in range(N - 2):
    for j in range(M - 2):
        if board_original[i][j] != board_result[i][j]:
            cnt += 1
            flip(i, j)

if chk():
    print(cnt)
else:
    print(-1)
