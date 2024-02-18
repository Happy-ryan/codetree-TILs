# 앞을 전부 반전시키는 유형의 그리디...뒤에서부터 파악!
# G -> 0, H -> 1
# s1 -> s2로 가즈아!
n = int(input())

s = []

for x1, x2 in zip(input(), input()):
    if x1 == x2:
        s.append(0)
    else:
        s.append(1)

# s를 0으로 만들기 위해 눌러야할 최소 횟수
cnt = 0
for idx in range(n - 1, -1, -1):
    if s[idx]:
        cnt += 1
        for i in range(idx, -1, -1):
            s[i] ^= 1

print(cnt)