N = int(input())

# table[i] = 자릿수가 i 일 때 0, 1, 2로 만들 수 있는 3의 배수의 수
table = [0] * (N + 1)

if N >= 2:
    # 자릿수가 늘어날 수록 생기는 3의 배수들은 이전 자릿수에서의 3의 배수 개수의 3배다
    table[2] = 2

    for i in range(3, N + 1):
        table[i] = (table[i - 1] * 3) % 1000000009

print(table[N])

