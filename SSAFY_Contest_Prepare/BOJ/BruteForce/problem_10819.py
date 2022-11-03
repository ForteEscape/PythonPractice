from itertools import permutations

N = int(input())
data = list(map(int, input().split()))

# 해당 data에서 만들 수 있는 모든 순열 조합을 만들어 그 합을 구한다.
per = permutations(data)
ans = 0
for element in per:
    sm = 0
    for j in range(len(element) - 1):
        sm += abs(element[j] - element[j + 1])
    ans = max(sm, ans)

print(ans)

