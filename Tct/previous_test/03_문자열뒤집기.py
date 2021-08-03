n = input()

count_0 = 0
count_1 = 0

start = n[0]
if start == '0':
    count_0 += 1
else:
    count_1 += 1

for i in range(1, len(n)):
    if start == n[i]:
        continue
    else:
        start = n[i]
        if start == '0':
            count_0 += 1
        else:
            count_1 += 1

print(min(count_0, count_1))

'''
change = 0
prev = '?'
string = input()
for i in string:
    if i != prev: change += 1
    prev = i
print(change//2)
'''
