import sys


N = int(sys.stdin.readline().rstrip())
dduck = sys.stdin.readline().rstrip()
s_cnt = 0
t_cnt = 0

for element in dduck:
    if element == 's':
        s_cnt += 1
    else:
        t_cnt += 1

idx = 0
new_dduck = ""

while s_cnt != t_cnt:
    new_dduck = dduck[idx:]

    if dduck[idx] == 's':
        s_cnt -= 1
    else:
        t_cnt -= 1

    idx += 1

print(dduck[idx:])