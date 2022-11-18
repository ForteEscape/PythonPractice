N = int(input())
data = []
for i in range(N):
    data.append((int(input()), i))

sorted_data = sorted(data)

ans = []
for i in range(N):
    ans.append(sorted_data[i][1] - data[i][1])

print(max(ans) + 1)