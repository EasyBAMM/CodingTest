from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# print(n, m)
# print(arr)
chickens = []
houses = []

for r in range(n):
    for c in range(n):
        if arr[r][c] == 1:
            houses.append((r, c))
        elif arr[r][c] == 2:
            chickens.append((r, c))

# 모든 m개를 뽑는 경우의 수
candidates = list(combinations(chickens, m))

city_distance = 1e9
# 경우의 수 중 하나씩 진행
for candidate in candidates:

    all_house = []
    # 각 집에서 치킨집까지 구해서 최소를 채택
    for hx, hy in houses:
        one_house = 1e9
        for cx, cy in candidate:
            one_house = min(one_house, abs(hx - cx) + abs(hy - cy))
        all_house.append(one_house)
    # 도시의 치킨 거리
    one_candidate = sum(all_house)
    # 경우의 수 비교
    city_distance = min(city_distance, one_candidate)

print(city_distance)
