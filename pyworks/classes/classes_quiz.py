# 실습 1 - 사칙연산 클래스 만들기
import sys


class Calculator:
    #

    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        if self.y == 0:
            print('0으로 나눌 수 없음')
            return sys.exit(0)
        else:
             return self.x / self. y


c1 = Calculator(5,10)
print(c1.add())
print(c1.sub())
print(c1.mul())
print(c1.div())


























