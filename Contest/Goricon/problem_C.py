N = int(input())

domino = []
for i in range(N):
    a, l = map(int, input().split())
    domino.append([a, l])

domino.sort(key=lambda x: x[0])

cnt = 1
for i in range(N - 1):
    if domino[i][0] < domino[i + 1][0] <= domino[i][0] + domino[i][1]:
        continue
    else:
        cnt += 1

print(cnt)