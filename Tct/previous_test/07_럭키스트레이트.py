n = list(input())
len_s = len(n)
left = n[0:len_s//2]
right = n[len_s//2:]

left = [int(i) for i in left]
right = [int(i) for i in right]

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")
