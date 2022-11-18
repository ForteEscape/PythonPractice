data = list(map(int, input().split()))
correct_data = [1, 1, 2, 2, 2, 8]

result = []
for i in range(6):
    result.append(correct_data[i] - data[i])

print(*result)