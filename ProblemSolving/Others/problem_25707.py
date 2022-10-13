import sys

N = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
data = sorted(data)

ans = 0

for i in range(N - 1):
    ans += abs(data[i + 1] - data[i])

ans += abs(data[-1] - data[0])
print(ans)