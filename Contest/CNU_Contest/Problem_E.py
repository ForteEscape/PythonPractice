import sys

N = int(sys.stdin.readline().rstrip())
dduck = sys.stdin.readline().rstrip()
is_visited = [False for _ in range(N)]
data = list(dduck)
length = len(data)
cnt = 0
ans = []


def is_palindrome(datalist):
    temp1 = ''
    temp2 = ''

    for element in datalist:
        temp1 += element

    for i in range(len(datalist) - 1, -1, -1):
        temp2 += datalist[i]

    return temp1 == temp2


def solve():
    global cnt
    if is_palindrome(data):
        ans.append(cnt)
        return

    for i in range(length):
        if not is_visited[i]:
            if data[i] == 's':
                temp = 's'
                replace = 't'
            else:
                temp = 't'
                replace = 's'

            is_visited[i] = True
            data[i] = replace
            cnt += 1
            solve()
            cnt -= 1
            data[i] = temp
            is_visited[i] = False


solve()
print(min(ans))
