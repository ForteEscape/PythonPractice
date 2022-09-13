import sys

N = int(input())

list_a = list(map(int, sys.stdin.readline().split()))
list_b = list(map(int, sys.stdin.readline().split()))

list_a = sorted(list_a)
list_b = sorted(list_b, reverse=True)

S = 0
for i in range(N):
    S += list_a[i] * list_b[i]

print(S)