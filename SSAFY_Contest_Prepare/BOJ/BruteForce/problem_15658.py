N = int(input())
data = list(map(int, input().split()))
operator_count = list(map(int, input().split()))
max_value = -1e9
min_value = 1e9


def solve(idx, ans, add, sub, mul, div):
    global max_value, min_value
    if idx >= N:
        max_value = max(max_value, ans)
        min_value = min(min_value, ans)
        return

    if add > 0:
        solve(idx + 1, ans + data[idx], add - 1, sub, mul, div)
    if sub > 0:
        solve(idx + 1, ans - data[idx], add, sub - 1, mul, div)
    if mul > 0:
        solve(idx + 1, ans * data[idx], add, sub, mul - 1, div)
    if div > 0:
        solve(idx + 1, int(ans / data[idx]), add, sub, mul, div - 1)


solve(1, data[0], operator_count[0], operator_count[1], operator_count[2], operator_count[3])
print(max_value)
print(min_value)
