# 학생 5명의 국, 수학 총점과 평균
score = [
    [80,70],
    [70,95],
    [60,90],
    [50,75],
    [75,60]
]

# 개인별 총점과 평균

# total = 0
students = []
n = len(score)
print('총점평균')
for i in range(0, n ) :
    # 총점 = 국어점수 + 수학점수
    # total(지역변수)은 필요할 곳에서 선언해서 사용
    # 블럭을 빠저나올때 소멸
    total = score[i][0] + score[i][1]
    students.append(total)
    print(total, total / 2)
print(students)


# 과목별 총점과 평균
# 국어 총점, 수학 총점, 국어 평군, 수학평균,
sum_subject = [0, 0] # 국어 총점, 수학 총점
avg_subject = [0.0, 0.0] # 국어 평균, 수학 평균

for i in range(0, n):
    sum_subject[0] += score[i][0]
    sum_subject[1] += score[i][1]

# 평균계산
avg_subject [0] = sum_subject  [0]  / n
avg_subject [1] = sum_subject  [1]  / n

print('국어 평균:', avg_subject[0])
print('수학 총점:', avg_subject[1])

















