N, M = map(int, input().split())
price = []

for i in range(M):
    package, individual = map(int, input().split())
    price.append([package, individual])

min_value = 1e9

if N < 6:
    for element in price:
        comparator = min(element[0], element[1] * N)
        min_value = min(min_value, comparator)

    print(min_value)
else:
    package = N // 6
    N = N % 6

    result = 0

    for element in price:
        comparator = min(element[0] * package, element[1] * (package * 6))
        min_value = min(min_value, comparator)

    result += min_value
    min_value = 1e9

    for element in price:
        comparator = min(element[0], element[1] * N)
        min_value = min(min_value, comparator)

    result += min_value
    print(result)