N = int(input())
height = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if height[i] == -1:
        continue
    cnt += 1
    pivot = height[i]

    for j in range(N):
        if pivot == height[j]:
            height[j] = -1
            pivot -= 1

print(cnt)
