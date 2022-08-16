import sys

N, M = map(int, sys.stdin.readline().split())
data = []
for _ in range(N):
    url, password = map(str, sys.stdin.readline().rstrip().split())
    data.append([url, password])

dict_data = dict(data)

for _ in range(M):
    key = sys.stdin.readline().rstrip()

    print(dict_data[key])