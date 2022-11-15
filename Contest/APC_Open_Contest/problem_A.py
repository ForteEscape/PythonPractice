N = int(input())
data = list(map(str, input().split()))

difficulty = {'B': 1, 'S': 2, 'G': 3, 'P': 4, 'D': 5}
difficulty_rev = {1: 'B', 2: 'S', 3: 'G', 4: 'P', 5: 'D'}
difficulty_data = []
for i in range(N):
    rank, rate = difficulty[data[i][0]], int(data[i][1:])
    difficulty_data.append([rank, rate])

result_data = sorted(difficulty_data, key=lambda x: (x[0], -x[1]))

is_trolled = False
ans = []
for i in range(N):
    if difficulty_data[i] != result_data[i]:
        is_trolled = True
        ans.append(result_data[i])

if is_trolled:
    print("KO")
    ans1 = difficulty_rev[ans[0][0]] + str(ans[0][1])
    ans2 = difficulty_rev[ans[1][0]] + str(ans[1][1])
    print(ans1, ans2)
else:
    print("OK")
