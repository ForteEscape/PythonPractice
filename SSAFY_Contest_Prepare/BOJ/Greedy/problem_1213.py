from collections import Counter

N = list(input())
N.sort()
chk = Counter(N)
cnt = 0

center = ''
for i in chk:
    # 문자 빈도 수가 홀수 개인 문자를 찾는다.
    if chk[i] % 2 != 0:
        cnt += 1
        center += i
        N.remove(i)

    # 문자 빈도 수가 홀수인 수의 개수가 1개 이상이라면, 회문을 만들 수 없다.
    if cnt > 1:
        break

if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    res = ""
    # 회문의 좌측 부분
    for i in range(0, len(N), 2):
        res += N[i]

    # 회문의 가운데(홀수 개의 빈도를 가진 문자) + 회문의 우측(좌측의 반대로 붙이면 된다.)
    print(res + center + res[::-1])
