import sys

N, M = map(int, sys.stdin.readline().split())
lalpha = list(map(int, sys.stdin.readline().split()))
other_streamer = [list(map(int, sys.stdin.readline().split())) for _ in range(N - 1)]
flag = False
idx = 0
cnt = 0

for i in range(N - 1):
    difference = 0
    for j in range(M):
        difference += abs(lalpha[j] - other_streamer[i][j])

    if difference > 2000:
        cnt += 1

    if ((N - 1) % 2 != 0 and (N - 1) // 2 < cnt) or ((N - 1) % 2 == 0 and (N - 1) // 2 <= cnt):
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")