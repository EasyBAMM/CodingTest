x, y, w, h = map(int, input().split())

t0 = w - x
t90 = h - y
t180 = x
t270 = y

print(min(t0, t90, t180, t270))
