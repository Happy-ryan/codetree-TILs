# 그리디 동전 유형 중 주어진 동전들이 배수인 경우
# 가치가 큰 동전부터 배부!
n, k = map(int, input().split())
moneys = [int(input()) for _ in range(n)]

cnt = 0
for money in moneys[::-1]:
    if k >= money:
        cnt += k // money
        k %= money

print(cnt)