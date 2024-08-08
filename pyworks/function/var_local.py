# 지역변수, 매개변수
# 스택구조
'''
메모리엣 순서(생성)
total
num2
num1

메모리에서 순서(소멸)
1. total 2. num2 3. num1
'''

def calc():
    x = 2 * num1
    print('x=', x)

# 지역변수
num1 = 10
num2 = 20
total = num1 + num2
calc()




























