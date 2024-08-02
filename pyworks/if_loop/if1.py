
# if문 - 조건: 나이가 15세 이상이면 '관람가' 출력

age = 17
'''
if age >= 15: #
    print("관람가")
print(f'나이는 {age}입니다.')
'''

age = 15
if age >= 15: #
    print("관람가")
else:
    print('관람불가')
print(f'나이는 {age}입니다.')



# 어떤 수를 짝수인지 홀수인지 판별하는 프로그램
# 짝수 -> 2의 배수 (2,4,6...) - 2로 나눈 나머지 0 <어떤수 % 2==0>
num = int(input('수를 입력하세요:'))
if num % 2 == 0:
    print('짝수')
else:
    print('홀수')
