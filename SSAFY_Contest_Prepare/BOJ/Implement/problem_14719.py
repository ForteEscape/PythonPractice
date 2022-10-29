N, M = map(int, input().split())
data = list(map(int, input().split()))
ans = 0

for i in range(1, M - 1):
    left_max = max(data[:i])
    right_max = max(data[i + 1:])

    height = min(left_max, right_max)

    if data[i] < height:
        ans += height - data[i]

print(ans)
