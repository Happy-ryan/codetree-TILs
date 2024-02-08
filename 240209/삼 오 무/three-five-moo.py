# n이 최대 10^9번째...n은 10^9버째를 찾기 위해서는 그것보다 훨 클 것!
n = int(input())
# 7이 4번째인 이유: 7번째인 7앞에 3의배수 2개, 5의 배수 1개가 있어서 7 - 3 = 4번쩨
# 숫자 n이 몇 번째인가? -3의배수 -5의배수 +15의배수

def find_seq(num: int):
    return num - num // 3 - num // 5 + num // 15

def binary_search(target_n: int):
    l, r = 1, int(1e15)
    ans = 1
    while l <= r:
        mid = (l + r) // 2
        if find_seq(mid) >= n:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans
    
print(binary_search(n))