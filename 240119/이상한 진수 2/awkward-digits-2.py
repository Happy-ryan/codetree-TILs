# 0이 존재..가장 큰 0을 1로 변경
# 0이 존재x..가장 작은 1을 0으로 변경
n = input()
max_val = 0

if '0' in n:
    # 가장 첫번째 '0'을 찾는다.
    idx = n.index('0')
    number = n[:idx] + '1' + n[idx+1:]
else:
    number = n[:-1] + '0'


cnt = 0
for idx, num in enumerate(number):
    cnt += (2 ** (len(number) - idx - 1)) * int(num)

print(cnt)