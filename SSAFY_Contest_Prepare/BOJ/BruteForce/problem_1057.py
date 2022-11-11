N, K, L = map(int, input().split())
ans = 0
is_right = False
while True:
    ans += 1
    if abs(K - L) == 1:
        for i in range(1, N + 1, 2):
            if K == i:
                if L == K + 1:
                    is_right = True
                    break
            elif L == i:
                if K == L + 1:
                    is_right = True
                    break
        if is_right:
            break

    if K != 1:
        if K % 2 == 0:
            K //= 2
        else:
            K = (K // 2) + 1

    if L != 1:
        if L % 2 == 0:
            L //= 2
        else:
            L = (L // 2) + 1

    if N % 2 == 0:
        N //= 2
    else:
        N = (N // 2) + 1

print(ans)