n = int(input())

grades = list(map(int, input().split()))
max_grade = max(grades)

for i in range(n):
    grades[i] = grades[i]/max_grade*100

print("%0.1f" % (sum(grades)/n))
