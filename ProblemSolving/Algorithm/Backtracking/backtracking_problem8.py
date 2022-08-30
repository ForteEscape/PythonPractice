import sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
ans = []
num_list = sorted(num_list)


def solve(cur_length):
    if cur_length == m:
        print(*ans)
        return

    for i in range(n):
        ans.append(num_list[i])
        solve(cur_length + 1)
        ans.pop()


solve(0)