# book - Tct 6장

n, m = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort()
arr_b.sort(reverse=True)

for i in range(m):
    if arr_a[i] < arr_b[i]:
        arr_a[i], arr_b[i] = arr_b[i], arr_a[i]
    else:
        break

print(sum(arr_a))
