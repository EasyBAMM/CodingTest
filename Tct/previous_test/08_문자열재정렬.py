s = list(input())
s.sort()

result = ""
for i in range(len(s)):
    if ord(s[i]) >= 65:
        break
result += ''.join(s[i:])
result += str(sum(map(int, s[:i])))

print(result)
