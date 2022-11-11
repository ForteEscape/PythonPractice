N, K = map(int, input().split())
data = list(input())

cnt = 0
for i in range(N):
    if data[i] == 'P':
        for j in range(i - K, i + K + 1):
            # OOB 검증
            if j < 0 or j >= N:
                continue
            # 위치에 햄버거가 있다면 즉시 먹는다.
            if data[j] == 'H':
                # 먹은 햄버거는 사라지므로 다르게 표시한다.
                data[j] = '-'
                cnt += 1
                break

print(cnt)
