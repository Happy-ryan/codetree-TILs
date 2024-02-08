# k개의 숫자라는 size가 고정..슬라이딩윈도우도 쌉가능할듯..?
# 존재하는 애들보다 사라진 애들에 초점을 맞추는게 필요함!
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


def prefix_sum(n, k, b, exclude):
    nums = list(range(1, n + 1))
    exclude_list = [0] * (n + 1)
    for x in exclude:
        exclude_list[x] = 1
    psum = [0] * (n + 2)
    for i in range(n + 1):
        psum[i + 1] = exclude_list[i] + psum[i]
    
    ans = k
    for i in range(n + 1 - k + 1):
        ans = min(ans, psum[i + k] - psum[i])

    return ans


# print(sliding_window(n, k, b, exclude))
print(prefix_sum(n, k, b, exclude))