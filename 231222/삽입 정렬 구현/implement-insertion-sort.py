n = int(input())
arr = list(map(int, input().split()))

def insertion_select(arr: list[int]) -> list[int]:
    n = len(arr)

    for i in range(1, n):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

print(*insertion_select(arr))