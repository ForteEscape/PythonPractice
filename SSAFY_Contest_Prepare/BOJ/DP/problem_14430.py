N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# table[y][x] = (y, x)까지 WOOK이 이동하였을 때 얻을 수 있는 최대 자원
table = [[0] * M for _ in range(N)]

# 초기값은 WOOK의 좌표 (0, 0)에서의 최대 자원이며 이는 (0, 0)이 0 또는 1에 의해 달라짐
table[0][0] = 0 if board[0][0] == 0 else 1

# 행, 열은 각각 자신의 왼쪽, 위쪽에서의 자원 최대값 + 현재 있는 장소의 자원에 대하여만 결정됨
for i in range(1, M):
    table[0][i] = table[0][i - 1] + board[0][i]

for i in range(1, N):
    table[i][0] = table[i - 1][0] + board[i][0]

# table[y][x]는 table[y - 1][x] 에서의 자원 최대값과 table[y][x - 1] 에서의 자원 최대값 중의 최대값이다.
for i in range(1, N):
    for j in range(1, M):
        table[i][j] = max(table[i - 1][j], table[i][j - 1]) + board[i][j]

print(table[N - 1][M - 1])