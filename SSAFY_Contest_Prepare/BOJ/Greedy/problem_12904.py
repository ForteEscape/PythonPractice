import copy

S = input()
T = list(input())
is_changeable = True
result = ''.join(T)

while len(result) != len(S):
    if T[-1] == 'A':
        del(T[-1])
    else:
        tmp_string = []
        for i in range(len(T) - 1, -1, -1):
            tmp_string.append(T[i])

        T = copy.deepcopy(tmp_string)

        if T[0] != 'B':
            is_changeable = False
            break
        else:
            del(T[0])
    result = ''.join(T)

if result != S:
    is_changeable = False

if is_changeable:
    print(1)
else:
    print(0)
