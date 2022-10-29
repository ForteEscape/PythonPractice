N, new_score, P = map(int, input().split())

if N == 0:
    print(1)
    exit(0)

ranking = list(map(int, input().split()))
ranking = sorted(ranking, reverse=True)

if N == P and ranking[-1] >= new_score:
    print(-1)
else:
    res = N + 1
    for i in range(N):
        if ranking[i] <= new_score:
            res = i + 1
            break
    print(res)