# 가면 매개 변수
# 매개변수 입력값이 정해지지 않는 변수임
# 변수이름앞에 '*' 를 붙인다.

def calc_avg(*numbers):
    sum_v = 0
    for i in numbers:
        sum_v = sum_v + i
        return sum_v / len(numbers)

avg1 = calc_avg(1, 2)
print(avg1)

avg1 = calc_avg(1, 2, 3, 4)
print(avg1)


