T = int(input())

while T:
    T -= 1
    R, C = map(int, input().split())
    white = 0

    if R != C:
        white = 1 * abs(C - R)
        weight = 2 * (2 + abs(R - C))
    else:
        white = 1
        weight = 4

    #1...n-1