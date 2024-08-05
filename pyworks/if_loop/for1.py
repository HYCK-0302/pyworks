#for 반복문
#초기값이 생략되면 0부터 시작
#끝값은 실제(끝값-1)임
#세번째 인자- 증감값
a = range(10)
print(list(a))

b = range(1, 11)
print(list(b))

c = range(1,11,2)
print(list(c))

#for문 - 1부터 10까지 출력
'''
for i in range(1, 11):
    print(i, end= ' ')
'''

#for 문 - 1부터 10까지 더하기(합계)
total = 0 #합계 저장 변수- 초기화 (0을저장)
for i in range(1, 100):
    #total = total + i
    total += i
    print('i',i,'total = ',total)
print(total)
