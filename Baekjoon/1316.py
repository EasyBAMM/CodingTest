n = int(input())

data = [input() for i in range(n)]

count = n
for s in data:
    len_s = len(s)
    alphabet = []
    for i in range(len_s):
        if s[i] not in alphabet:
            alphabet.append(s[i])
        else:
            if s[i] != s[i-1]:
                count -= 1
                break

print(count)
