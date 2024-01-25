n = int(input())
dp = [-1] * (n + 1)
mod = 10007

# dpf(n) = 1 * dpf(n - 1) + 2 * dpf(n - 2)

def dpf(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    
    if dp[n] != -1:
        return dp[n]
        
    ret = dpf(n - 1) % mod + 2 * dpf(n - 2) % mod
    ret %= mod

    dp[n] = ret

    return ret


print(dpf(n))