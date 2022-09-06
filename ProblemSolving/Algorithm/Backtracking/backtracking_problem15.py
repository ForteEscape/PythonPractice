# 암호 만들기
import sys

L, C = map(int, sys.stdin.readline().split())
code = list(map(str, sys.stdin.readline().split()))

code = sorted(code)
is_used = [False for _ in range(C)]

ans = []
cnt_vowels = 0
cnt_cons = 0


def solve(code_length):
    global cnt_vowels
    global cnt_cons

    if code_length == L:
        if cnt_vowels >= 1 and cnt_cons >= 2:
            print("".join(ans))
        return

    for i in range(C):
        if not is_used[i]:
            if not ans:
                is_used[i] = True
                ans.append(code[i])

                if code[i] in ['a', 'e', 'i', 'o', 'u']:
                    cnt_vowels += 1
                else:
                    cnt_cons += 1

                solve(code_length + 1)

                if ans[-1] in ['a', 'e', 'i', 'o', 'u']:
                    cnt_vowels -= 1
                else:
                    cnt_cons -= 1

                ans.pop()
                is_used[i] = False
            else:
                if code[i] > ans[-1]:
                    is_used[i] = True
                    ans.append(code[i])

                    if code[i] in ['a', 'e', 'i', 'o', 'u']:
                        cnt_vowels += 1
                    else:
                        cnt_cons += 1

                    solve(code_length + 1)

                    if ans[-1] in ['a', 'e', 'i', 'o', 'u']:
                        cnt_vowels -= 1
                    else:
                        cnt_cons -= 1

                    ans.pop()
                    is_used[i] = False


solve(0)
