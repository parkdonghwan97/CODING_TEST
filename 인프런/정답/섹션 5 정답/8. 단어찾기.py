# import sys
# sys.stdin = open('input.txt')

# from collections import deque


# n = int(input())

# a = []
# answer = []
# for i in range(n):
#     a.append( input()   ) 

# dq = deque(a)   

# # print(dq)     deque(['big', 'good', 'sky', 'blue', 'mouse'])

# for i in range(n-1):

#     x = input()   #  sky good mouse big

#     if x in dq:  # x안에 있으면 answer에 넣고
#         answer.append(x)

#     else: # 있으면 pass
#         pass 

#     # 처음에 없으면 answer에 넣으려했는데 없는데 ,,, 없으면 못넣음 ^^;;;
        
# for i in dq :
#     if i not in answer:
#         print(i)



################ 강사님 코드

# dict로 해서 한번 쓰이면 1로 바꿈 

n = int(input()  )

p = dict()  # { k : v }

for i in range(n):
    word = input()
    p[word]= 0      # word라는 키의 값을 0로 설정 


for i in range(n-1):
    word = input()
    p[word] = 1


##  처음 딕셔너리의 value은 모두 0이다. 
# 하지만 밑에서 한 번씩 쓰인 단어들의 value은 1로 변경되었을 것이다.
# 
# 즉 딕셔너리의 value가 0인  키를 찾으면 된다. 

for k, v in p.items():
    
    if v == 0:
        print(k)





