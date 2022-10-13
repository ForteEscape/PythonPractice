import sys

N, M = map(int, sys.stdin.readline().split())

while True:
    M += N
    if M >= 5:
        print("yt")
        break

    N += M
    if N >= 5:
        print("yj")
        break
