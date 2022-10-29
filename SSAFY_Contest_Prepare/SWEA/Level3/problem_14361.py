# 14361번 숫자가 같은 배수
T = int(input())

for test_case in range(1, T + 1):
    N = input()
    str_data = list(N)
    size = new_size = len(N)
    num_N = int(N)
    cnt = 2
    is_possible = False

    while new_size == size:
        is_possible = True
        data = num_N * cnt
        cnt += 1

        data = str(data)

        if len(data) > size:
            is_possible = False
            break

        new_size = len(data)
        for element in data:
            if element not in str_data:
                is_possible = False
                break
        else:
            print(f"#{test_case} possible")
            break

    if not is_possible:
        print(f"#{test_case} impossible")