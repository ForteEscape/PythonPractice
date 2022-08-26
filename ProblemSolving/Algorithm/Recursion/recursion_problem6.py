import sys

N = int(sys.stdin.readline().rstrip())
image = [list(map(str, sys.stdin.readline())) for _ in range(N)]
ans = ""


def chk(x, y, n):
    for i in range(y, y + n):
        for j in range(x, x + n):
            if image[y][x] != image[i][j]:
                return 0

    return image[y][x]


def solve(x, y, N):
    global ans
    if chk(x, y, N):
        ans += str(chk(x, y, N))
        return

    ans += "("
    size = int(N / 2)

    for i in range(2):
        for j in range(2):
            solve(x + j * size, y + i * size, size)

    ans += ")"


solve(0, 0, N)
print(ans)