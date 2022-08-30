import sys

n, m = map(int, sys.stdin.readline().split())
num_list = [x for x in range(1, n + 1)]
ans = []


def solve(cur_length):
    if cur_length == m:
        print(*ans)
        return

    for i in range(n):
        if ans and num_list[i] < ans[-1]:
            continue

        ans.append(num_list[i])
        solve(cur_length + 1)
        ans.pop()


solve(0)
