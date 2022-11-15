N, M, Q = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 0:
        arr[query[1]][query[2]] = query[3]
    else:
        arr[query[1]], arr[query[2]] = arr[query[2]], arr[query[1]]

for element in arr:
    print(*element)