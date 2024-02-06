s = int(input())

def sum_val(n):
    cnt = 0
    for x in range(1, n + 1):
        cnt += x
    return cnt

# s 보다 작은 1 ~ n까지의 합에서 n의 최댓값
def binary_search(target: int):
    l, r = 0, target
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if sum_val(mid) <= target:
            ans = mid
            l += 1
        else:
            r -= 1

    return ans

print(binary_search(s))