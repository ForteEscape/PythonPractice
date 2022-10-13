N = int(input())

for i in range(1, 100000):
    if i % 2 != 0 and N < i:
        print(i - N)
        break
    elif i % 2 == 0 and N < i:
        print("0")
        break

    N -= i
