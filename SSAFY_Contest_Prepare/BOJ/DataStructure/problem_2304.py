N = int(input())
location = [0 for _ in range(1001)]
end = -1

for _ in range(N):
    x, height = map(int, input().split())
    location[x] = height

    if end < x:
        end = x

mx_height = max(location)
mx_idx = location.index(mx_height)

area = 0
pivot = 0
# 좌에서 우로
for i in range(mx_idx + 1):
    if location[i] > pivot:
        pivot = location[i]
    area += pivot

pivot = 0
for i in range(end, mx_idx, -1):
    if location[i] > pivot:
        pivot = location[i]
    area += pivot

print(area)