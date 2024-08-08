#과제1
'''
a= ['게토레이','레스비','생수','이프로']

while True:
    print('============RESTART')
    b=input('마시고 싶은 음료?')
    if b in a:
        a.remove(b)
        print(b, '드릴게요')
        print('남은 음료는 ', a)
    else:
        print(f'{b}는 지금 없네요')
 '''
# 과제2
a= ['게토레이','레스비','생수','게토레이','이프로','생수']

while True:
    who = input('사용자 종류 입력하세요: \n1.소비자, \n2.주인\n')
    if who == '1':
        b = input('마시고 싶은 음료?')
        if b in a:
            a.remove(b)
            print(b, '드릴게요')
            print('남은 음료는 ', a)
        else:
            print(f'{b}는 지금 없네요')
    elif who == '2':
        todo = input('할 일 선택(1. 추가 , 2. 삭제): ')
        if todo == '1':
            print('남은 음료는 ', a)
            d = input('추가할 음료수?')

        elif todo == '2':
            print('남은 음료는')
            d=input('삭제할 음료수?')
            if d in a:
                print('삭제완료')
                print('남은 음료는')
            else:
                print('없음')





























