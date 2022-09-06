# 연산자 끼워넣기
import sys

N = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().split()))
oper_list = list(map(int, sys.stdin.readline().split()))
operation = ["+", "-", "x", "/"]
num_max = -1000000001
num_min = 1000000001
fomula = []


def solve(depth):
    if depth == N - 1:
        idx = 1
        result = num_list[0]
        for i in range(N - 1):
            if fomula[i] == "+":
                result += num_list[idx]
                idx += 1
            elif fomula[i] == "-":
                result -= num_list[idx]
                idx += 1
            elif fomula[i] == "x":
                result *= num_list[idx]
                idx += 1
            elif fomula[i] == "/":
                if result < 0:
                    result *= -1
                    result = result // num_list[idx]
                    idx += 1
                    result *= -1
                else:
                    result = result // num_list[idx]
                    idx += 1

        global num_min
        global num_max
        if num_min > result:
            num_min = result

        if num_max < result:
            num_max = result

        return

    for i in range(4):
        if oper_list[i] != 0:
            fomula.append(operation[i])
            oper_list[i] -= 1
            solve(depth + 1)
            oper_list[operation.index(fomula[-1])] += 1
            fomula.pop()

    return


solve(0)
print(num_max)
print(num_min)
