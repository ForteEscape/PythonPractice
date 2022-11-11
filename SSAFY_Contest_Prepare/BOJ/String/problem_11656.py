N = input()
data = []

for i in range(len(N)):
    data.append(N[i:])

data.sort()
for i in range(len(data)):
    print(data[i])