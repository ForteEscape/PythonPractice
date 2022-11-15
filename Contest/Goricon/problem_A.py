T = int(input())

while T > 0:
    T -= 1

    N = int(input())
    mission = [list(map(int, input().split())) for _ in range(N)]

    K, D, A = map(int, input().split())
    result = 0

    for element in mission:
        data = element[0] * K + element[2] * A - element[1] * D
        if data > 0:
            result += data

    print(result)
