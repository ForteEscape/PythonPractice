import sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list = sorted(num_list)
ans = []


def solve(cur_length):
    if cur_length == m:
        print(*ans)
        return

    temp = 0
    for i in range(n):
        if ans:
            if temp != num_list[i] and num_list[i] >= ans[-1]:
                ans.append(num_list[i])
                temp = num_list[i]
                solve(cur_length + 1)
                ans.pop()
        else:
            if temp != num_list[i]:
                ans.append(num_list[i])
                temp = num_list[i]
                solve(cur_length + 1)
                ans.pop()


solve(0)
