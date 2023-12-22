n = int(input())
numbers = [0] + list(map(int, input().split()))

ans = 0
j = 0
count_array = [0] * (max(numbers) + 1)

for i in range(1, n + 1):
    while j + 1 <= n and count_array[numbers[j + 1]] != 1:
        count_array[numbers[j + 1]] += 1
        j+= 1

    ans = max(ans, j - i + 1)
    count_array[numbers[i]] -= 1


print(ans)