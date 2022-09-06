# 로또
import sys

ans = []
is_used = [False for _ in range(12)]


def solve(cur_length, length, numbers):
    if cur_length == 6:
        print(*ans)
        return

    for i in range(length):
        if not is_used[i]:
            if not ans:
                is_used[i] = True
                ans.append(numbers[i])
                solve(cur_length + 1, length, numbers)
                ans.pop()
                is_used[i] = False
            else:
                if numbers[i] > ans[-1]:
                    is_used[i] = True
                    ans.append(numbers[i])
                    solve(cur_length + 1, length, numbers)
                    ans.pop()
                    is_used[i] = False


while True:
    data = list(map(int, sys.stdin.readline().split()))
    k = data[0]

    if k == 0:
        break

    num_list = data[1:]
    solve(0, k, num_list)
    print("")
    