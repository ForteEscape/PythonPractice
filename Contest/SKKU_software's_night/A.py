import sys

N, X = map(int, sys.stdin.readline().split())
voice_lim = list(map(int, sys.stdin.readline().split()))

cnt = 0
while True:
    if voice_lim[cnt % N] < X:
        print(cnt % N + 1)
        break
    cnt += 1
    X += 1