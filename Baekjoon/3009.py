x_ = []
y_ = []

for i in range(3):
    x, y = map(int, input().split())
    x_.append(x)
    y_.append(y)

nx = 0
ny = 0
for i in range(3):
    if x_.count(x_[i]) == 1:
        nx = x_[i]
    if y_.count(y_[i]) == 1:
        ny = y_[i]

print(nx, ny)
