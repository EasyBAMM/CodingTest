while True:
    d1, d2, d3 = map(int, input().split())
    if d1*d2*d3 == 0:
        break

    dall = [d1, d2, d3]
    Heru = max(dall)
    Ausar = min(dall)
    Auset = sum(dall) - Heru - Ausar

    if Heru**2 == Ausar**2 + Auset**2:
        print("right")
    else:
        print("wrong")
