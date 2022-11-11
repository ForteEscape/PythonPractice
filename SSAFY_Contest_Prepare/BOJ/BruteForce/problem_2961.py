from itertools import combinations

N = int(input())
status = []
ans = 1e9

for i in range(N):
    sweet, bitter = map(int, input().split())
    status.append([sweet, bitter])

for i in range(1, N + 1):
    comb = combinations(status, i)

    for element in comb:
        sweet_data, bitter_data = 1, 0
        for data in element:
            sweet_data *= data[0]
            bitter_data += data[1]

        ans = min(ans, abs(sweet_data - bitter_data))

print(ans)