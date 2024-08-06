# 자료구조- 딕셔너리 dictionary
# "치킨" : "닭을 튀긴 요리" key(키) : value(값)
# {} 중괄호 사용

fruits = ['apple0','banana','cherry']
fruits = {
    'apple': '사과',
    'banana' : '바나나',
    'peach' : '복숭아'

}

# 접근(검색)
print(fruits['apple'])
# print(fruits['tomato']) # key Error발생

# get()을 이용한 검색
print(fruits.get('banana')) # none

# 요소 추가
fruits["stawberry"] = '딸기'
print(fruits)
print(type(fruits)) # dict

# 요소 수정

fruits['peach'] = "천도복숭아"
print(fruits)

# 요소 삭제
fruits.pop('banana')
print(fruits)

# 키만 반환
print(fruits.keys())

# 값만 반환
print(fruits.values())

# 키와 값 모두 반환
print(fruits.items())

# 키와 값 전체 조회
for key in fruits:
    print(key,':',fruits[key])

# 딕셔너리 생성
dict1 = {1:'a',2:'b',3:'c'}
print(dict1)

# key=4, value='d' 추가

dict1[4] = 'd'
print(dict1)

#  for 문을 이용한 전체 조회

for key in dict1.keys():
    print(f'{key}: {dict1[key]}')

# 요소수정 - key 3을 'k' 로 변경

dict1[3] = 'k'
print(dict1)

# 요소 삭제 - key 2 삭제
dict1.pop(2)
print(dict1)


# 빈 딕셔너리 생성
dict2 = {} # 빈 딕셔너리
print(dict2)


dict2["mike"]= 10
print(dict2)





