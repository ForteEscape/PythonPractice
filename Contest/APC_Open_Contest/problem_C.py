N = int(input())
data_dict = []
match_str = {}
for _ in range(N):
    data = input()
    data_dict.append(data)

M = int(input())
raw_data = list(map(str, input().split()))

for i in range(N):
    if len(data_dict[i]) != 1:
        key = data_dict[i][0] + data_dict[i][-1]
    else:
        key = data_dict[i]

    match_str[key] = data_dict[i]

ans = []
for element in raw_data:
    if len(element) == 1:
        key = element
    else:
        key = element[0] + element[-1]
    ans.append(match_str[key])

print(*ans)