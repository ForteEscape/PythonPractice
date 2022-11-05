N, K = map(int, input().split())

result = 0
data = []
ans_list = []


def solve(ans):
    if ans == N:
        ans_str = ''
        ans_str += str(data[0])
        for i in range(1, len(data)):
            ans_str += '+'
            ans_str += str(data[i])

        ans_list.append(ans_str)
        return

    if ans > N:
        return

    for i in range(1, 4):
        data.append(i)
        ans += i

        solve(ans)

        ans -= i
        data.pop()


solve(0)
if K - 1 >= len(ans_list):
    print(-1)
else:
    print(ans_list[K - 1])