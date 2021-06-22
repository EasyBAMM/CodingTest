import re
from collections import Counter
import copy

str1 = "handshake"
str2 = "shake hands"

# 공백제거, 모두 대문자 통일
str1 = str1.upper()
str2 = str2.upper()
str1 = re.sub(r"[^a-zA-Z]", "", str1)
str2 = re.sub(r"[^a-zA-Z]", "", str2)

# 2글자씩 추출
set_a = [str1[i:i+2] for i in range(len(str1)-1)]
set_b = [str2[i:i+2] for i in range(len(str2)-1)]

set_a = [re.sub(r"[^a-zA-Z]", "", x) for x in set_a]
set_b = [re.sub(r"[^a-zA-Z]", "", x) for x in set_b]

print("set_a: ", set_a)
print("set_b: ", set_b)

set_count_a = dict(Counter(set_a))
set_count_b = dict(Counter(set_b))
set_count_intersection = {}
set_count_union = copy.deepcopy(set_count_b)

print("set_count_a: ", set_count_a)
print("set_count_b: ", set_count_b)

for key in set_count_a.keys():
    if key in set_count_b:
        set_count_intersection[key] = min(set_count_a[key], set_count_b[key])
        set_count_union[key] = max(set_count_a[key], set_count_b[key])
    else:
        set_count_union[key] = set_count_a[key]

print("set_count_intersection: ", set_count_intersection)
print("set_count_union: ", set_count_union)

set_count_intersection_sum = sum(set_count_intersection.values())
set_count_union_sum = sum(set_count_union.values())

print("set_count_intersection_sum: ", set_count_intersection_sum)
print("set_count_union_sum: ", set_count_union_sum)


if set_count_intersection_sum == 0 and set_count_union_sum == 0:
    result = 1 * 65536
else:
    result = int(set_count_intersection_sum / set_count_union_sum * 65536)

print(result)
