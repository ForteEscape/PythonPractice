import sys

n, m = map(int, sys.stdin.readline().split())
num_list = [x for x in range(1, n + 1)]
ans = []


def solve(cur):
    if cur == m:
        print(*ans)
        return

    for i in range(n):
        ans.append(num_list[i])
        solve(cur + 1)
        ans.pop()


solve(0)