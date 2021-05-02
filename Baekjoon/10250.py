case = int(input())

for x in range(case):
    h, w, n = map(int, input().split())
    room = [[0 for j in range(w)] for i in range(h)]

    floors = n % h
    ho = n // h + 1

    if floors == 0:
        floors += h

    if n % h == 0:
        ho -= 1

    room_number = floors*100 + ho
    print(room_number)
