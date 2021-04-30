from collections import Counter

input_ = input().upper()

count_input = dict(Counter(input_))

values = list(count_input.values())

if len(values) == 1:
    print(input_)
else:
    values.sort()
    if values[-1] == values[-2]:
        print("?")
    else:
        max_key = max(count_input.keys(), key=lambda x: count_input[x])
        print(max_key)
