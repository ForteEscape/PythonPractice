N, M = map(int, input().split())

S = set()
for i in range(N):
    data = input()
    S.add(data)

cnt = 0
for i in range(M):
    comparator = input()
    if comparator in S:
        cnt += 1

print(cnt)