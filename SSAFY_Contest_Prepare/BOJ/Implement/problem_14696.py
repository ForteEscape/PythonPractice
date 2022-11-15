N = int(input())

for _ in range(N):
    player1_data = list(map(int, input().split()))
    player2_data = list(map(int, input().split()))

    card_data = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for i in range(1, player1_data[0] + 1):
        card_data[0][player1_data[i]] += 1

    for i in range(1, player2_data[0] + 1):
        card_data[1][player2_data[i]] += 1

    for i in range(4, 0, -1):
        if card_data[0][i] > card_data[1][i]:
            print("A")
            break
        elif card_data[0][i] < card_data[1][i]:
            print("B")
            break
    else:
        print("D")

