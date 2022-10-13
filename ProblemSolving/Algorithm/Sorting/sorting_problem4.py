import sys

length = []
visit = [False for _ in range(9)]
for i in range(9):
    L = int(sys.stdin.readline().rstrip())
    length.append(L)

length = sorted(length)
ans = []
flag = False


def answer(amount, s):
    global flag
    if flag:
        return

    if amount == 7:
        if s == 100:
            flag = True
            for i in ans:
                print(i)

        return

    for i in range(9):
        if not visit[i]:
            visit[i] = True
            amount += 1
            s += length[i]
            ans.append(length[i])

            answer(amount, s)

            ans.pop()
            s -= length[i]
            amount -= 1
            visit[i] = False


answer(0, 0)