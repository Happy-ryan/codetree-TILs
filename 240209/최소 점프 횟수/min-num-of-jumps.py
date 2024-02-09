n = int(input())
nums = list(map(int, input().split()))
min_val = 11

ans = []
def dfs(idx: int):
    global min_val
    if idx == n - 1:
        min_val = min(min_val, len(ans))
        return


    for val in range(1, nums[idx] + 1):
        new_idx = idx + val
        ans.append(nums[new_idx])
        dfs(new_idx)
        ans.pop()
        
        
dfs(0)
print(min_val)