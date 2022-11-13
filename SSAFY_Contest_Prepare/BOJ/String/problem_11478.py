data = input()
dataset = []

for i in range(len(data)):
    for j in range(i, len(data)):
        temp = data[i:j + 1]
        dataset.append(temp)

print(len(set(dataset)))