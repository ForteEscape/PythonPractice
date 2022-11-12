T = int(input())

# 가장 큰 인덱스를 중앙으로 하여 양옆을 그 다음으로 큰 인덱스들로 채운다.
while T > 0:
    T -= 1

    N = int(input())
    logs = list(map(int, input().split()))
    logs.sort()

    result = 0
    for j in range(2, N):
        # index = 2일때 통나무간 높이 차가 가장 작게 난다.
        result = max(result, abs(logs[j] - logs[j - 2]))
    print(result)