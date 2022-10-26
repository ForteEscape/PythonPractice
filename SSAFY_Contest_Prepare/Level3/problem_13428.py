# 13428 숫자 조작
T = int(input())

for test_case in range(1, T + 1):
    N = input()
    num_list = []

    data = list(N)
    for i in range(len(data)):
        temp, idx = -1, -1
        for j in range(i + 1, len(data)):
            if int(data[i]) < int(data[j]):
                if temp <= int(data[j]):
                    temp = int(data[j])
                    idx = j
        if temp != -1:
            tmp = data[i]
            data[i] = data[idx]
            data[idx] = tmp
            break

    mx_value = ''.join(data)

    data = list(N)
    for i in range(len(data)):
        temp, idx = 10, -1
        for j in range(i + 1, len(data)):
            if int(data[i]) > int(data[j]):
                if i == 0 and int(data[j]) == 0:
                    continue
                elif i == 0 and int(data[j]) != 0:
                    if temp >= int(data[j]):
                        temp = int(data[j])
                        idx = j
                else:
                    if temp >= int(data[j]):
                        temp = int(data[j])
                        idx = j
        if temp != 10:
            tmp = data[i]
            data[i] = data[idx]
            data[idx] = tmp
            break

    mn_value = ''.join(data)

    print(f"#{test_case} {mn_value} {mx_value}")