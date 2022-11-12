N = int(input())
data_str = input()
data = data_str.split('*')
dataset = []

for _ in range(N):
    dataset.append(input())

for i in range(len(dataset)):
    substr1 = dataset[i][:len(data[0])]
    substr2 = dataset[i][-len(data[1]):]

    if len(dataset[i]) >= (len(data_str) - 1) and substr1 == data[0] and substr2 == data[1]:
        print("DA")
    else:
        print("NE")