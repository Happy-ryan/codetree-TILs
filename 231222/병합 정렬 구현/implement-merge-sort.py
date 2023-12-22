n = int(input())
arr = list(map(int, input().split()))

def merge_sort(arr: list[int]):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left: list[int], right: list[int]):
    new_array = []

    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            new_array.append(right[r])
            r += 1
        else:
            new_array.append(left[l])
            l += 1

    new_array.extend(left[l:])
    new_array.extend(right[r:])

    return new_array

print(*merge_sort(arr))