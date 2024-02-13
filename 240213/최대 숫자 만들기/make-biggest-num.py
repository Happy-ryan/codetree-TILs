from functools import cmp_to_key

# o1 앞, o2 뒤 
# compare의 기본: 오름차순(o1 - o2 < 0: -1) 
# 내림차순!!! (o1 - o2 > 0: -1)
# -1이 있는 if문이 현재의 차순을 나타냄.
# def compare(o1, o2):
#     if o1 - o2 == 0:
#         return 0
#     if o1 - o2 > 0:
#         return 1
#     if o1 - o2 < 0:
#         return -1

n = int(input())
nums = [input() for _ in range(n)]

def compare(o1, o2):
    # 4 43
    # 443, 434
    new_o1 = o1 + o2
    new_o2 = o2 + o1
    if int(new_o1) - int(new_o2) == 0:
        return 0
    if int(new_o1) - int(new_o2) > 0:
        return -1
    if int(new_o1) - int(new_o2) < 0:
        return 1

nums.sort(key=cmp_to_key(compare))

print(''.join(nums))