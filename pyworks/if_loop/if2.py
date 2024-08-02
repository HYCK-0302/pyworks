# 다중조건
'''
if  조건1:
    실행문(조건 1 참일 떄)
elif 조건2:
    실행문(조건 2 참일 때)
leif:
    실행문(조건1과 2가 모두 거짓일 때)
'''

age = 25
if age < 20:
    print('미성년자 입니다')
elif age < 30:
    print('20대 입니다')
elif age < 40:
    print('30대 입니다')
else:
    print('이제는 중년 입니다')
print(f'나이는{age}세 입니다.')

