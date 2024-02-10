# 조합

n, m = map(int, input().split())
nums = list(map(int, input().split()))


def xor_cal(arr: list[int]):
    ans = 1
    for x in arr:
        ans ^= x
    return ans

# nCm..n과 m이 정해짐..
ans = []
max_val = 0
def combination(cur_idx, cnt):
    global max_val
    if cur_idx == n:
        if cnt == m:
            max_val = max(max_val, xor_cal(ans))
        return

    ans.append(nums[cur_idx])
    combination(cur_idx + 1, cnt + 1)
    ans.pop()

    combination(cur_idx + 1, cnt)
    
combination(0, 0)
print(max_val)