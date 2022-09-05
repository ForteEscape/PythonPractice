import sys, copy

n, m, k = map(int, sys.stdin.readline().split())
note = [[0 for _ in range(m)] for _ in range(n)]


def is_pastable(x, y, paper, r, c):
    for i in range(r):
        for j in range(c):
            if note[y + i][x + j] == 1 and paper[i][j] == 1:
                return False

    for i in range(r):
        for j in range(c):
            if paper[i][j] == 1:
                note[y + i][x + j] = 1

    return True


def rotate(paper, r, c):
    rotate_list = [[0 for _ in range(r)] for _ in range(c)]

    for i in range(c):
        for j in range(r):
            rotate_list[i][j] = paper[r-1-j][i]

    return rotate_list, c, r


for i in range(k):
    paper_r, paper_c = map(int, sys.stdin.readline().split())
    paper = [list(map(int, sys.stdin.readline().split())) for _ in range(paper_r)]

    for rotate_cnt in range(4):
        is_paste = False
        for y in range(n - paper_r + 1):
            if is_paste:
                break
            for x in range(m - paper_c + 1):
                if is_pastable(x, y, paper, paper_r, paper_c):
                    is_paste = True
                    break

        if is_paste:
            break
        paper, paper_r, paper_c = rotate(paper, paper_r, paper_c)

cnt = 0
for i in range(n):
    for j in range(m):
        if note[i][j] == 1:
            cnt += 1

print(cnt)
