import sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
ans = []

is_used = [False for _ in range(n)]
num_list = sorted(num_list)


def solve(cur_length):
    if cur_length == m:
        print(*ans)
        return

    for i in range(n):
        if ans:
            if not is_used[i] and num_list[i] > ans[-1]:
                is_used[i] = True
                ans.append(num_list[i])
                solve(cur_length + 1)
                is_used[i] = False
                ans.pop()
        else:
            is_used[i] = True
            ans.append(num_list[i])
            solve(cur_length + 1)
            is_used[i] = False
            ans.pop()


solve(0)
