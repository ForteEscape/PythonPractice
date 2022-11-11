N = int(input())
max_sum = 0
positive_data = []
negative_data = []

for _ in range(N):
    data = int(input())
    if data <= 0:
        negative_data.append(data)
    elif data == 1:
        max_sum += 1
    else:
        positive_data.append(data)

positive_data.sort(reverse=True)
negative_data.sort()

# 양수 리스트의 길이가 짝수인 경우
if len(positive_data) % 2 == 0:
    for i in range(0, len(positive_data), 2):
        max_sum += positive_data[i] * positive_data[i + 1]
# 홀수인 경우
else:
    for i in range(0, len(positive_data) - 1, 2):
        max_sum += positive_data[i] * positive_data[i + 1]
    max_sum += positive_data[-1]

# 음수의 경우 작을 수록 곱할 시 더해지는 값은 커진다 따라서 맨 마지막을 더하는 게 맞다.(홀수 길이일 경우)
if len(negative_data) % 2 == 0:
    for i in range(0, len(negative_data), 2):
        max_sum += negative_data[i] * negative_data[i + 1]
else:
    for i in range(0, len(negative_data) - 1, 2):
        max_sum += negative_data[i] * negative_data[i + 1]
    max_sum += negative_data[-1]

print(max_sum)



