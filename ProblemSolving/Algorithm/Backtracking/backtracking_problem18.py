# 계란으로 계란치기
import sys

N = int(sys.stdin.readline().rstrip())
eggs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
brake_cnt = 0
cnt_max = -100001


def solve(current_egg):
    global brake_cnt
    global cnt_max
    if current_egg == N:
        if brake_cnt > cnt_max:
            cnt_max = brake_cnt
        return

    if eggs[current_egg][0] <= 0 or brake_cnt == N - 1:
        solve(current_egg + 1)
        return

    for i in range(N):
        if i == current_egg or eggs[i][0] <= 0:
            continue

        eggs[current_egg][0] -= eggs[i][1]
        eggs[i][0] -= eggs[current_egg][1]

        if eggs[current_egg][0] <= 0:
            brake_cnt += 1
        if eggs[i][0] <= 0:
            brake_cnt += 1

        solve(current_egg + 1)

        if eggs[current_egg][0] <= 0:
            brake_cnt -= 1
        if eggs[i][0] <= 0:
            brake_cnt -= 1

        eggs[current_egg][0] += eggs[i][1]
        eggs[i][0] += eggs[current_egg][1]


solve(0)
print(cnt_max)