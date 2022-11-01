T = int(input())

while T != 0:
    T -= 1

    N = int(input())
    price = list(map(int, input().split()))
    result = 0

    pivot = price[-1]
    for i in range(N - 2, -1, -1):
        if price[i] >= pivot:
            pivot = price[i]
        else:
            result += pivot - price[i]

    print(result)
