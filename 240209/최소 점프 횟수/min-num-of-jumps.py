n = int(input())
nums = list(map(int, input().split()))
min_val = 11

ans = []
def dfs(idx: int):
    global min_val
    if idx == n - 1:
        # print(ans)
        min_val = min(min_val, len(ans))
        return


    for val in range(1, nums[idx] + 1):
        new_idx = idx + val
        if new_idx < n:
            ans.append(nums[new_idx])
            dfs(new_idx)
            ans.pop()
        
        
dfs(0)

ans = min_val
if ans >= 11:
    ans = -1

print(ans)