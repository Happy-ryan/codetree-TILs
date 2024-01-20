levels = list(map(int, input().split()))

min_level = 100000000
ans = []
def dfs(level, idx):
    global min_level
    if level == 3:
        k = abs(2 * sum(ans) - sum(levels))
        min_level = min(min_level, k)
        return

    for idx in range(idx, len(levels)):
        ans.append(levels[idx])
        dfs(level + 1, idx + 1)
        ans.pop()

dfs(0, 0)

print(min_level)