
print('Hello~')

# 인사하는 함수 - greet
# new
def greet():
    print('안녕~')   # 지역 영역

def greeting(name):
    print('안녕~',name)

def get_gugudan(dan):
    for i in range(1,10) :
        print(f'{dan}x{i}={dan * i}')

#  구구단 호출
get_gugudan (4)  # dan = 4



# 메인 영역(실행영역)
greet()   #호출

#메인 영역(실행영역)
greet()  #호출

# 더하는 함수 호출

add(10,11)












