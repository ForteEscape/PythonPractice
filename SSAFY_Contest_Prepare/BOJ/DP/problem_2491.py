N = int(input())
data = list(map(int, input().split()))

# dp[i] = i번째 수 직전까지의 증/감소 수열의 길이
dp = [[1] * N for _ in range(2)]

for i in range(1, N):
    if data[i - 1] <= data[i]:
        dp[0][i] = dp[0][i - 1] + 1
    if data[i - 1] >= data[i]:
        dp[1][i] = dp[1][i - 1] + 1

# 2차원 리스트의 최대값 구하는 간편한 방법
print(max(map(max, dp)))
