from math import *


def factorial(N):
    if N <= 1:
        return N
    else:
        return N * factorial(N - 1)


def exponential(x, N):
    if N <= 0:
        return 1
    else:
        result = (x ** N) / factorial(N)
        return result + exponential(x, N - 1)


print(exponential(2, 10))
print(exp(2))


def sine(x, N):
    if N == 0:
        return x
    else:
        result = (((-1) ** N) * (x ** (2 * N + 1))) / factorial((2 * N + 1))
        return result + sine(x, N - 1)


print(sine(2, 10))
print(sin(2))


def cosine(x, N):
    if N == 0:
        return 1
    else:
        result = (((-1) ** N) * (x ** (2 * N))) / factorial(2 * N)
        return result + cosine(x, N - 1)


print(cosine(2, 10))
print(cos(2))