# global- 전역변수임을 알려준는 키워드
# 전역변수는 값을 유지하고 공유함
def one_up():
    global x
    x +=1
    return x


x = 0 #전역변수
print(one_up()) #1
print(one_up()) #2
print(one_up()) #3
print('x=',x)


def get_price(10000,3)

    print('상픔1가격':)