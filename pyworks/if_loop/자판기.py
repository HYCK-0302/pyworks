#과제1

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