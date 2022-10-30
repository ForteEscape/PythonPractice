enhance_rate = []
visited = [False for _ in range(9)]

for i in range(10):
    N = float(input())
    enhance_rate.append(N)

enhance_rate = sorted(enhance_rate, reverse=True)

cnt = 9
ans = 1
for i in range(9):
    ans *= (enhance_rate[i] / cnt)
    cnt -= 1

print(round(ans * (10 ** 9), 6))
