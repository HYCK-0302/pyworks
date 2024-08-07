# 학색 3명의 성적 통계
student = [
    {'name':'이대한','kor':90,'math': 85},
    {'name':'반믹국','kor':80,'math': 75},
    {'name':'윤지능','kor':95,'math': 90},

]
'''

# print(student)
# print(student[0])
# print(student[-1])
print('개인별 평균 점수')
print('이름 국어 수학 평균')
for std in student :
    sum_score = std["kor"] + ['math'] # 개인별 총점
    avg_score = sum_score / 2
    print(f'{std['name']}   { std['kor']} {std['name']} { avg_score:.1f}')
'''




# 학색 3명의 성적 통계
student = [
    {'name':'이대한','kor':90,'math': 85},
    {'name':'반믹국','kor':80,'math': 75},
    {'name':'윤지능','kor':95,'math': 90},

]
# print(student)
# print(student[0])
# print(student[-1])
print('국어 총점')
print('수학 총점')
for std in student :
    sum_score = std["kor"] + std['math'] # 개인별 총점
    avg_score = sum_score / 2
    print(f'{std['name']}   { std['kor']} {std['name']} { avg_score:.1f}')


print('과목별 총점과 평균')
kor_total = 0
math_total = 0
for i in student:
    kor_total= kor_total + i['kor']
    math_total += i['math']
print("국어 총점: ", kor_total)
print('수학총점',math_total)

print('국어평균', round(kor_total / len(student), 2))
print("수학평균",round(math_total/ len(student), 2))
























































