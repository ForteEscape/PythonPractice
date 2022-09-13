N = input()

hex_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
number_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
num = 1
ans = 0

for i in (len(N) - 1, -1, -1):
    idx = hex_list.index(N[i])
    ans += num * number_list[idx]
    num *= 16

print(ans)


