# 나이를 숫자로 입력해주세요
#결제 방법을 입력해주새요
# age, payment, fee
age = int(input("숫자로 입력해주세요"))
payment = input('결제방법을 입력해주새요')
fee = ""

if age < 8 :
    fee="무료"
elif age < 14 :
    fee= '450원'
elif age < 20 :
    if payment == '카드':
        fee= '720원'
    else:
        fee= '1000원'
elif age < 75 :
    if payment == '카드':
        fee='1200원'
    else:
        fee= '1300'
else:
    fee= '무료'
print(f"{age}세의 {payment}요금은 {fee}입니다")






















