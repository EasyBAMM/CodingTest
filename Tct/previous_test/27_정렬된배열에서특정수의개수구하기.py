from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
numbers = list(map(int, input().split()))

length = len(numbers)
left = bisect_left(numbers, x)
right = bisect_right(numbers, x)

if left == length:
    print(-1)
else:
    print(right - left)

# def bisearch_left(numbers, find_x, low, high):

#     while low < high:
#         mid = (low + high) // 2

#         if numbers[mid] < find_x:
#             low = mid + 1
#         else:
#             high = mid

#     return low


# def bisearch_right(numbers, find_x, low, high):

#     while low < high:
#         mid = (low + high) // 2

#         if find_x < numbers[mid]:
#             high = mid
#         else:
#             low = mid + 1

#     return low
