import sys

S, T = map(int, sys.stdin.readline().split())
dp = [0 for _ in range(T + 1)]


def get_divisor(N):
    data = {}

    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0: # N // i
            pass


    return even, odd


ans = []
for i in range(S, T + 1):
    even, odd = get_divisor(i)
    ans.append((1 * even) + (-1 * odd))

print(sum(ans))