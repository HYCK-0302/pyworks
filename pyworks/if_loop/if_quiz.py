# 실습 1

# 조건 - 시내에서 자동차의 주행속도가 50km 이상이면 "속도 위반입니다" 출력하고
# 아니면 "규졍 속도 준수!!"를 출력하새요.
# 주행속도 - 60km임

speed = int(input('속도를 입력하세요.'))

if speed >= 50:
    print('속도위반입니다.')
else:
    print('규정속도를 준수')
