T = int(input())
table = [[1, 0], [0, 1], [1, 1]]


def fibo(N):
    length = len(table)
    if N >= length:
        for i in range(length, N + 1):
            table.append([table[i - 1][0] + table[i - 2][0], table[i - 1][1] + table[i - 2][1]])

    print('{} {}'.format(table[N][0], table[N][1]))


while T > 0:
    T -= 1

    N = int(input())
    fibo(N)
