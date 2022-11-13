N = int(input())
mx_length = -1e9
mx_data = []


def make_seq(data):
    idx = 2
    while True:
        result = data[idx - 2] - data[idx - 1]
        if result < 0:
            break

        data.append(result)
        idx += 1

    return idx, data


for i in range(1, N + 1):
    temp = [N, i]
    length, result_data = make_seq(temp)

    if length > mx_length:
        mx_length = length
        mx_data = result_data

print(mx_length)
print(*mx_data)