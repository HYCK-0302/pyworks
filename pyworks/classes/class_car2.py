# 생성자 (construuctor)
class Car:
    def __init__ (self,model,year):
        self.model = model  #외우기
        self.year = year

    def show_info(self):
        print(f'모델명:{self.model},연식:{self.year}')

# car_a 는 메모리 힙(heap)을 사용한다.
'''
car_a = Car('아이오닉6',2023)
car_a.show_info()
'''

'''
car_a = Car('스포티지',2023)
car_a.show_info()
'''

# 객체 리스트 만들기
cars = [
    Car('소나타',2020),
    Car('k5',2017),
    Car('모닝',2022),

]
cars[0].show_info()
cars[-1].show_info()
print('******* 승용차 list ******')
for car in cars:
    car.show_info()






















