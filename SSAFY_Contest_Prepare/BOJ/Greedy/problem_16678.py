N = int(input())
honer = [int(input()) for _ in range(N)]
honer.sort()
cnt = 0

cnt += honer[0] - 1
honer[0] = 1

for i in range(1, N):
    if honer[i] - honer[i - 1] > 1:
        cnt += (honer[i] - honer[i - 1] - 1)
        honer[i] = honer[i - 1] + 1

print(cnt)
