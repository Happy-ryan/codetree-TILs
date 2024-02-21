# n = int(input())
# nums = list(map(int, input().split()))
# min_val = 11

# ans = []
# def dfs(idx: int):
#     global min_val
#     if idx == n - 1:
#         min_val = min(min_val, len(ans))
#         return


#     for val in range(1, nums[idx] + 1):
#         new_idx = idx + val
#         if new_idx < n:
#             ans.append(nums[new_idx])
#             dfs(new_idx)
#             ans.pop()
        
        
# dfs(0)

# ans = min_val
# if ans >= 11:
#     ans = -1

# print(ans)

n = int(input())
jumps = list(map(int, input().split()))

ans = []
inf = int(1e9)
min_ans = inf
def dfs(idx):
    global min_ans
    if idx == n - 1:
        min_ans = min(min_ans, len(ans))
        return
    
    for jump in range(1, jumps[idx] + 1):
        if idx + jump < n:
            ans.append(jump)
            dfs(idx + jump)
            ans.pop()
        
dfs(0)
if min_ans >= inf:
    min_ans = -1
print(min_ans)