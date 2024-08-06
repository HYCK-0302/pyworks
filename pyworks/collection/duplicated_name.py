# 리스트, set을 사용 -중복 이름 찾기
name = ['흥부','콩쥐','놀부','콩쥐']

duplicated_name = set() # 빈 셋을 생성
n = n=len(name)
for i in range(0, n-1): #n=4
    for j in range(i+1, n):    #중복패턴i+1
        if name[1] == name[j]:
            duplicated_name.add(name[i])

'''
    i=0,    j=1 , name[0] == [1]  '흥부'== '콩쥐'
            j=2 , name[0] == [2]  '흥부'== '놀부'
            j=3 , name[0] == [3]  '흥부'== '콩쥐'
    i=1     j=2 , name[1] == [2]  '콩쥐'== '놀부'   
            j=3 , name[1] == [3]  '콩쥐'== '콩쥐'    '중복!!'
    i=2     j=3 , name[2] == [3]  '놀부'== '콩쥐'     
'''
print(f'중복이름:{duplicated_name}')
















