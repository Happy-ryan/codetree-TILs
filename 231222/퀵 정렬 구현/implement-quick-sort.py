n = int(input())
arr = list(map(int, input().split()))

def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr

    pivot = arr[len(arr)//2]

    left, middle, right = [], [], []

    for number in arr:
        if number > pivot:
            right.append(number)
        elif number < pivot:
            left.append(number)
        else:
            middle.append(number)

    return quick_sort(left) + middle + quick_sort(right)


print(*quick_sort(arr))