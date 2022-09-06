# N-M 유형 3
import sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
is_used = [False for _ in range(n)]

num_list = sorted(num_list)
ans = []


def solve(cur_length):
    if cur_length == m:
        print(*ans)
        return

    temp = 0
    for i in range(n):
        if not is_used[i] and temp != num_list[i]:
            is_used[i] = True
            ans.append(num_list[i])
            temp = num_list[i]
            solve(cur_length + 1)
            ans.pop()
            is_used[i] = False


solve(0)


