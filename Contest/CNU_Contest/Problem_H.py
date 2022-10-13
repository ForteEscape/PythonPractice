import sys

N = int(sys.stdin.readline().rstrip())
size_list = list(map(int, sys.stdin.readline().split()))
size_list = sorted(size_list)
is_absorbed = [False for _ in range(N)]

ans = N

for i in range(N):
    for j in range(i + 1, N):
        if size_list[i] < size_list[j] and not is_absorbed[j]:
            is_absorbed[j] = True
            ans -= 1
            break

print(ans)