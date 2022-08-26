import sys
# calculate a^b mod n


def power(a, b, n):
    if b == 1:
        return a % n

    data = power(a, int(b/2), n)
    data = data * data % n

    if b % 2 == 0:
        return data

    return data * a % n


a, b, c = map(int, sys.stdin.readline().split())
print(power(a, b, c))