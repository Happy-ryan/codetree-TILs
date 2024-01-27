n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[1], x[0]))

# print(arr)

last = arr[0][1]
cnt = 1
for start, end in arr[1:]:
    if last < start:
        # print(start, end)    
        cnt += 1
        last = end

print(cnt)