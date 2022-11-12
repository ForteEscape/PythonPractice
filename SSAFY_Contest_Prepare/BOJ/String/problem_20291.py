N = int(input())

file_infix = {}
for _ in range(N):
    data = input().split('.')

    if data[1] not in file_infix:
        file_infix[data[1]] = 1
    else:
        file_infix[data[1]] += 1

file_infix = sorted(file_infix.items())

for element in file_infix:
    print(element[0], element[1])