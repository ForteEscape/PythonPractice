M, N = map(int, input().split())
t = int(input())

width = [0, M]
height = [0, N]

for _ in range(t):
    s, l = map(int, input().split())

    if s == 0:
        height.append(l)
    else:
        width.append(l)

width.sort()
height.sort()

result = 0

for i in range(len(width) - 1):
    for j in range(len(height) - 1):
        x = width[i + 1] - width[i]
        y = height[j + 1] - height[j]
        result = max(result, x * y)

print(result)