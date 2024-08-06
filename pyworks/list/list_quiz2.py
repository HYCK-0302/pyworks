# 실습 5

# sum()
# print(sum([1,2,3]))
# print(max)([1,2,3]))

input_num = input('숫자 여러 개 입력:').split(' ')
numbers = [] # 숫자를 저장할 리스트
for i in input_num:
    numbers.append(int(i))
print(numbers)


print(f'가장 큰 값: {max(numbers)}')
print(f'가장 작은 값: {min(numbers)}')
print(f'나머지 값의 평균: {(sum(numbers)-(max(numbers)+min(numbers))) /  (len(numbers)-2)}')