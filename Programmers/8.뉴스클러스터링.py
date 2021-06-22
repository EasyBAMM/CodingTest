from collections import Counter
import copy

str1 = "aa1+aa2"
str2 = "AAAA12"


# 2글자씩 추출
set_a = [str1[i:i+2] for i in range(len(str1)-1)]
set_b = [str2[i:i+2] for i in range(len(str2)-1)]

# 공백제거, 모두 대문자 통일
set_a = [x for x in set_a if x.isalpha()]
set_a = [x.upper() for x in set_a]
set_b = [x for x in set_b if x.isalpha()]
set_b = [x.upper() for x in set_b]


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


'''
def solution(str1, str2):
    from collections import Counter
    import copy
    
    # 2글자씩 추출
    set_a = [str1[i:i+2] for i in range(len(str1)-1)]
    set_b = [str2[i:i+2] for i in range(len(str2)-1)]

    # 공백제거, 모두 대문자 통일
    set_a = [x for x in set_a if x.isalpha()]
    set_a = [x.upper() for x in set_a]
    set_b = [x for x in set_b if x.isalpha()]
    set_b = [x.upper() for x in set_b]


    # print("set_a: ", set_a)
    # print("set_b: ", set_b)

    # 문자 카운트
    set_count_a = dict(Counter(set_a))
    set_count_b = dict(Counter(set_b))
    set_count_intersection = {}
    set_count_union = copy.deepcopy(set_count_b)

    # print("set_count_a: ", set_count_a)
    # print("set_count_b: ", set_count_b)

    for key in set_count_a.keys():  # a에서 key뽑기
        if key in set_count_b:  # b에 있으면
            set_count_intersection[key] = min(set_count_a[key], set_count_b[key])
            set_count_union[key] = max(set_count_a[key], set_count_b[key])
        else:   # b에 없으면
            set_count_union[key] = set_count_a[key]

    # print("set_count_intersection: ", set_count_intersection)
    # print("set_count_union: ", set_count_union)

    set_count_intersection_sum = sum(set_count_intersection.values())
    set_count_union_sum = sum(set_count_union.values())

    # print("set_count_intersection_sum: ", set_count_intersection_sum)
    # print("set_count_union_sum: ", set_count_union_sum)


    if set_count_intersection_sum == 0 and set_count_union_sum == 0:
        result = 1 * 65536
    else:
        result = int(set_count_intersection_sum / set_count_union_sum * 65536)

    return result
'''
