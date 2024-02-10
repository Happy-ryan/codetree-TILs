n, m = map(int, input().split())

ans = []
def back(level, idx):
    if level == m:
        print(*ans)
        return


    for i in range(idx, n + 1):
        if len(ans) == 0 or ans[-1] < i:
            ans.append(i)
            back(level + 1, idx + 1)
            ans.pop()

back(0, 1)