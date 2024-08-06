# 다중 if 실습
# 점수가 마이너스일 경우 '올바른 점수를 입력해 주세요'
score = '' #빈문자열
score = int(input('점수입력'))
'''

if score > 0 :
    if score >= 90:  # 0 < age <0
        print('A등급입니다')
    elif score >= 80:
        print('B등급입니다')
    elif score >= 70:
        print('C등급입니다')
    elif score >= 60:
        print('D등급입니다')
    else:
        print('E등급입니다')
else:
    print('올바른 점수를 입력해주세요')
'''

if score < 0 :
else:
    if score > 0:
        if score >= 90:  # 0 < age <0
            print('A등급입니다')
        elif score >= 80:
            print('B등급입니다')
        elif score >= 70:
            print('C등급입니다')
        elif score >= 60:
            print('D등급입니다')
        else:
            print('E등급입니다')
    else:
        print('올바른 점수를 입력해주세요')


