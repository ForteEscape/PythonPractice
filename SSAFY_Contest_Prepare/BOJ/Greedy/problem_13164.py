N, K = map(int, input().split())
data = list(map(int, input().split()))

diff = []
for i in range(N - 1):
    diff.append(data[i + 1] - data[i])

diff.sort(reverse=True)
print(sum(diff[K - 1:]))
