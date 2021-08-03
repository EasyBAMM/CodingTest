import heapq
import sys

input = sys.stdin.readline
n = int(input())
cards = []
for i in range(n):
    cards.append(int(input()))


result = 0
heapq.heapify(cards)

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    c = a+b
    heapq.heappush(cards, c)
    result += (c)

print(result)
