import sys

n, m = map(int, sys.stdin.readline().split())
num_list = [x for x in range(1, n + 1)]
is_used = [False for _ in range(n)]
ans = []


def solve(cur):
    if cur == m:
        print(*ans)
        return

    for i in range(n):
        if not ans:
            if not is_used[i]:
                is_used[i] = True
                ans.append(num_list[i])
                solve(cur + 1)
                is_used[i] = False
                ans.pop()
        else:
            if not is_used[i] and num_list[i] > ans[-1]:
                is_used[i] = True
                ans.append(num_list[i])
                solve(cur + 1)
                is_used[i] = False
                ans.pop()


solve(0)
