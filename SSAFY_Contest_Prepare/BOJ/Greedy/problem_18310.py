N = int(input())
location = list(map(int, input().split()))

location.sort()
ans = N // 2 if N % 2 == 0 else N // 2 + 1

print(location[ans - 1])