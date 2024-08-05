# 실습
#홀수 합만 구하기
#출력 결과
''''
#for 문 - 1부터 10까지 더하기(합계)
a= int(input("어디까지계산할까요?"))
total = 0 #합계 저장 변수- 초기화 (0을저장)
for i in range(1,a+1):
    #total = total + i
    total += i
print(total)
'''

'''
#실습2
#입력한 숫자만큼 카운트하고 “발사“ 출력
count=int(input("숫자입력"))+1
while True :
    count=count -1
    if count < 1:
        break
    print(count, end=' ')
print('발사')
'''

a= int(input('몇까지 합을 계산할까요?'))
total = 0
for i in range (a,0,+1):
    if i % 2== 1:  # 1, 2, 3, 4, 5
        total += i
print(f'1부터{a}까지의 합: {total}')
