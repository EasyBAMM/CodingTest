def solution(scoville, K):
    import heapq

    heapq.heapify(scoville)
    answer = 0

    while scoville[0] < K:
        try:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            new = a + (b*2)
            heapq.heappush(scoville, new)
        except IndexError:
            return -1
        answer += 1

    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))


# def solution(scoville, K):
#     import heapq
#     answer = 0

#     heap = []
#     for num in scoville:
#         heapq.heappush(heap, num)

#     while heap[0] < K:
#         try:
#             heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
#         except IndexError:
#             return -1
#         answer += 1
#     return answer
