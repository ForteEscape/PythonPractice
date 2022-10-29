# problem 15230 알파벳 공부

T = int(input())
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

for test_case in range(1, T + 1):
    idx = 0
    data = input()

    for element in data:
        if element != alphabet[idx % 26]:
            break
        idx += 1

    print(f"#{test_case} {idx}")