def binary_search(numbers, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if numbers[mid] == mid:
        return mid
    elif numbers[mid] > mid:
        return binary_search(numbers, low, mid - 1)
    else:
        return binary_search(numbers, mid + 1, high)


n = int(input())
numbers = list(map(int, input().split()))

print(binary_search(numbers, 0, len(numbers)))
