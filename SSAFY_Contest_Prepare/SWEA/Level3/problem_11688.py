# 11688 Calkin-Wilf tree 1
import math

T = int(input())

for test_case in range(1, T + 1):
    cmd = input()
    a, b = 1, 1

    for element in cmd:
        if element == 'L':
            b = a + b
        elif element == 'R':
            a = a + b

    chk = math.gcd(a, b)
    if chk == 1:
        print("#{} {} {}".format(test_case, a, b))
    else:
        a = a // chk
        b = b // chk

        print("#{} {} {}".format(test_case, a, b))