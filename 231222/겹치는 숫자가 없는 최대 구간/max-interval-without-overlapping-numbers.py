n = int(input())
# 0. two-pointer: 1base가 되도록...
numbers = [0] + list(map(int, input().split()))

# 1. 변수 선언
ans = 0
count_array = [0] * (max(numbers) + 1)
# 2. 구간 설정
j = 0
for i in range(1, n + 1):
    # 3. 같은 숫자가 2개 되기 전까지 반복!
    while j + 1 <= n and count_array[numbers[j + 1]] < 1:
        count_array[numbers[j + 1]] += 1
        j+= 1
    
    # 4. 현재 구간 [i, j] = j - 1 + 1
    ans = max(ans, j - i + 1)
    # 5. 다음 구간으로 넘어가기 위해서 numbers[i] 제외
    count_array[numbers[i]] -= 1


print(ans)