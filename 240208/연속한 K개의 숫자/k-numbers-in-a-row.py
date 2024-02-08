# k개의 숫자라는 size가 고정..슬라이딩윈도우도 쌉가능할듯..?
n, k, b = map(int, input().split())
exclude = [int(input()) for _ in range(b)]

def sliding_window(n, k, b, exclude):
    nums = list(range(1, n + 1))
    exclude_list = [0] * (n + 1)
    for x in exclude:
        exclude_list[x] = 1
    # 최대 k를 추가해야할 수 있음.
    ans = k
    # 초기값
    # 1base
    l = 1
    r = l + k - 1
    cnt = sum(exclude_list[l: r + 1])
    while r < n:
        # 슬라이딩 윈도우는 기존l과 새로운r이 중요하다!
        cnt -= exclude_list[l]
        l += 1
        r += 1
        cnt += exclude_list[r]

        ans = min(ans, cnt)
    
    return ans

print(sliding_window(n,k,b,exclude))