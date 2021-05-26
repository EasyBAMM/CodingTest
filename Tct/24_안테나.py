n = int(input())

house = list(map(int, input().split()))
house.sort()

middle = len(house) // 2

print(house[middle-1])
