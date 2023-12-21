n = int(input())
arr = list(map(int, input().split()))

def bubbl_sort(arr: list[int]) -> list[int]:
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break
    return arr

print(*bubbl_sort(arr))