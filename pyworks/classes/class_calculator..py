

class Calculator:
    def __init__(self):
        self.x = 0  # 멤버변수, 인스턴스 변수(지역변수)

    def add(self,y):
        self.x = self.x + y
        return self.x

    def sub(self,y):
        self.x = self.x - y
        return self.x


c1 = Calculator()
print(c1.x)
print(c1.add(10))
print(c1.sub(5))











