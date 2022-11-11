S = int(input())
data = list(map(int, input().split()))
N = int(input())

if N in data:
    print(0)
    exit(0)

data.append(N)
data.sort()
pivot = data.index(N)
if pivot == 0:
    start = 0
else:
    start = data[pivot - 1]
end = data[pivot + 1]
ans = 0

for i in range(start + 1, N + 1):
    for j in range(N, end):
        if i < j:
            ans += 1

print(ans)