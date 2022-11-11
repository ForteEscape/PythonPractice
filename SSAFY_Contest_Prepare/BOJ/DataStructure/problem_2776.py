T = int(input())

while T != 0:
    T -= 1

    N = int(input())
    note1 = list(map(int, input().split()))

    M = int(input())
    note2 = list(map(int, input().split()))

    dataset = set(note1)
    for element in note2:
        if element not in dataset:
            print(0)
        else:
            print(1)

# set의 in 연산 복잡도가 list의 in 연산 복잡도보다 작다.
