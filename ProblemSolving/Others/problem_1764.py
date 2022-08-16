import sys

N, M = map(int, sys.stdin.readline().split())
dict_not = {}

for _ in range(N):
    name = sys.stdin.readline().rstrip()
    dict_not[name] = 0

cnt = 0
ans = []
for _ in range(M):
    name = sys.stdin.readline().rstrip()

    for key in dict_not.keys():
        if key == name:
            cnt += 1
            ans.append(key)

print(cnt)
for element in ans:
    print(element)

