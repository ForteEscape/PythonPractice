import sys

N, M = map(str, sys.stdin.readline().split())

new_N, new_M = '', ''

for i in N:
    if i == '6':
        new_N += '5'
        continue
    new_N += i

for j in M:
    if j == '6':
        new_M += '5'
        continue
    new_M += j

mn = int(new_M) + int(new_N)

new_N, new_M = '', ''

for i in N:
    if i == '5':
        new_N += '6'
        continue
    new_N += i

for j in M:
    if j == '5':
        new_M += '6'
        continue
    new_M += j

mx = int(new_M) + int(new_N)

print(mn, mx)
