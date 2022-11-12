N = int(input())
in_dataset = {}
cnt = 0

for i in range(N):
    data = input()
    in_dataset[data] = i

out_dataset = []
for i in range(N):
    data = input()
    out_dataset.append(data)

for i in range(N - 1):
    for j in range(i + 1, N):
        if in_dataset[out_dataset[i]] > in_dataset[out_dataset[j]]:
            cnt += 1
            break

print(cnt)
