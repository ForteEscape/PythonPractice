import sys

N = int(sys.stdin.readline().rstrip())
paper_status = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = [0, 0, 0]


def chk(x, y, n):
    for i in range(y, y + n):
        for j in range(x, x + n):
            if paper_status[y][x] != paper_status[i][j]:
                return False

    return True


def paper(N, c, r):
    if chk(c, r, N):
        ans[paper_status[r][c] + 1] += 1
        return
    N = int(N / 3)

    for i in range(3):
        for j in range(3):
            paper(N, c + j * N, r + i * N)


paper(N, 0, 0)
for index in ans:
    print(index)