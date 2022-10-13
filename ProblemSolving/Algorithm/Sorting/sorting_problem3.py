import sys

T = int(sys.stdin.readline().rstrip())

while T:
    T -= 1
    N = int(sys.stdin.readline().rstrip())
    phone = [sys.stdin.readline().rstrip() for _ in range(N)]
    phone = sorted(phone)
    flag = False

    for i in range(N - 1):
        length = len(phone[i])

        if phone[i] == phone[i + 1][:length]:
            flag = True
            break

    if flag:
        print("NO")
    else:
        print("YES")
