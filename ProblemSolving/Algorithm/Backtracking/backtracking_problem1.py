import sys

n, m = map(int, sys.stdin.readline().split())
num_list = [x for x in range(1, n + 1)]
is_used = [False for _ in range(0, n)]
seq = []


def solve(cur_length):
    if cur_length == m:
        print(*seq)

    for i in range(n):
        if not is_used[i]:
            is_used[i] = True
            seq.append(num_list[i])
            solve(cur_length + 1)
            is_used[i] = False
            seq.pop()


solve(0)


