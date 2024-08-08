# 실습1번 문제
# (2.2) 매개변수전달하여 서로 같으면 곱하고 다르면 더하는 함수
'''
def square (a,b) :
    if a == b :
        return a*b
    else:
        return a+b
print("결과(곱):", square(2,2))
print("결과(합):", square(2,3))


#실습 2
def get_price(price,count):
    if price * count <20000:
        return price * count +2500
    else:
         return price * count
print(f'상품1 가격: {get_price(10000,3)}')
print(f'상품2 가격: {get_price(5000,3)}')
'''


'''
# 실습 4
def times3():
    count = 0
    for i in range(1,31):
        if i % 3 == 0:
            print(i, end=' ')
            count = count + 1
    print()
    print(f'3의 배수의 개수:{count}')

times3()
'''

# 실습 3
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
'''
a = ['게토레이', '레스비', '생수', '게토레이', '이프로', '생수']

def check_machine():
    print(f'남은 음료는? {a}')
def is_drink(drink):
    if drink in a :
        print(f'{drink}있습니다')
    else:
        print(f'{drink}없습니다')

def add_drink(drink):
    a.append(drink)
    print(f'남은 음료수는 {a}')
def remove_drink(drink):
    a.remove(drink)
    print(f'남은 음료수는 {a}')

check_machine()
is_drink('콜라')
add_drink('환타')
remove_drink('생수')


_





