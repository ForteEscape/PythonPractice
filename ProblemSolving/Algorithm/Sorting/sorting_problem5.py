import sys

T = int(sys.stdin.readline().rstrip())

while T != 0:
    T -= 1
    ans = 1

    N = int(sys.stdin.readline().rstrip())
    rank_list = []
    for i in range(N):
        rank1, rank2 = map(int, sys.stdin.readline().split())
        rank_list.append([rank1, rank2])

    rank_list = sorted(rank_list, key=lambda x: x[0])

    pivot = rank_list[0][1]

    for i in range(1, N):
        if rank_list[i][1] < pivot:
            pivot = rank_list[i][1]
            ans += 1

    print(ans)