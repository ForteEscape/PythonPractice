n = int(input())


def hanoi(pillar1, pillar2, n):
    if n == 1:
        print(pillar1, pillar2)
        return

    hanoi(pillar1, 6 - pillar1 - pillar2, n - 1)
    print(pillar1, pillar2)
    hanoi(6 - pillar1 - pillar2, pillar2, n - 1)


print((2 ** n) - 1)
hanoi(1, 3, n)