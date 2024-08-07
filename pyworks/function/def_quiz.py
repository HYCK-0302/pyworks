# 실습1번 문제
# (2.2) 매개변수전달하여 서로 같으면 곱하고 다르면 더하는 함수
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














