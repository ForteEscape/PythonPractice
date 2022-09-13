import sys

N, M, K = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
number = sorted(number, reverse=True)
ans = 0

first = number[0]
second = number[1]

while M != 0:
    for i in range(K):
        if M == 0:
            break
        ans += first
        M -= 1

    if M == 0:
        break

    ans += second
    M -= 1

print(ans)


