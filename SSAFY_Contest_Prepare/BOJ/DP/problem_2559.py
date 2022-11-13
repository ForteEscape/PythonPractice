# 메모지제이션 dp 유형은 아니나 prefix sum 및 sliding window기법 사용해서 해당 유형으로 분류함

N, K = map(int, input().split())
data = list(map(int, input().split()))

if K == 1:
    print(max(data))
    exit(0)
elif K == N:
    print(sum(data))
    exit(0)

ans = -1e9
result = sum(data[:K])
ans = max(ans, result)
for i in range(K, N):
    result -= data[i - K]
    result += data[i]
    ans = max(ans, result)

print(ans)