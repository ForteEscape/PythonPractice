N = int(input())
fibo_list = [-1 for _ in range(55)]
fibo_list[0] = 0
fibo_list[1] = 1


def fibo(n):
    if n == 0 or n == 1:
        return n

    if fibo_list[n] != -1:
        return fibo_list[n]

    fibo_list[n] = fibo(n - 1) + fibo(n - 2)
    return fibo_list[n]


print(fibo(N))