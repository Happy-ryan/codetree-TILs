n = int(input())
card_b = [int(input()) for _ in range(n)]
card_b.sort()

memo = [0 for _ in range(n)]

for i in range(n):
    memo[i] = 2 * n - card_b[i] - (n - i - 1)

# 상대편의 가장 큰 값부터 제거
# 우리의 가장 큰 카드도 죽기 때문에 중간에 반드시 지는 경우가 존재함!
# 사용한 카드수를 기록해야한다.
# 나보다 큰 값 - 뽑을 수 있는 카드의 수(memo[val])> 사용한 카드의 수(used)
used_card_num = 0
score = 0
for val in range(n - 1, -1, -1):
    if memo[val] > 0 and memo[val] > used_card_num:
        score += 1
        used_card_num += 1
    #     print(f"나의 위치: {memo[val]}, 사용한 카드 수: {used_card_num}")
    # else:
    #     print(f"내가 쓸 수 있는 카드 수: {memo[val]} < 사용한 카드 수: {used_card_num}")
print(score)