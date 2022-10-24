import sys

N = int(sys.stdin.readline().rstrip())
weight = list(map(int, sys.stdin.readline().split()))
ans = 0

l = len(weight)
pivot = weight[-1]

for i in range(l - 2, -1, -1):
    if weight[i] <= pivot:
        ans = max(ans, pivot - weight[i])
    else:
        pivot = weight[i]

print(ans)