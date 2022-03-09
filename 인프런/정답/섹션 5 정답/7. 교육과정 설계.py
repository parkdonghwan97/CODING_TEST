# import sys
# sys.stdin = open('input.txt')


# 80 점짜리 정답 .  이거 대체 왜 오류지
# from collections import deque


# b= input()
# a = b
# n = int(input())



# answer =[]

# for i in range(n):
#     a = deque(b)

#     x = input()
    


#     for j in x:        # CBDAGE
#         x = deque(x)
#         tmp = x.popleft()    # C   B      D    A


#         if tmp == a[0] :   # CBA  BA      A    A
#             a.popleft()    # BA    A           ' '

#             if len(a) ==0:
#                 break
                

#     if len(a) == 0 :
#         # print('#',i+1, 'YES' , end='')  
#         answer.append( ('#{} YES').format(i+1)    )

#     else:
#         # print('#',i+1, 'NO')
#         answer.append( ('#{} NO').format(i+1)    )
        

# for i in answer:
#     print(i)

from collections import deque


need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)


    for x in plan:

        if x in dq:

            if x!=dq.popleft():
                print('#%d NO' %(i+1))
                break

    else:
        if (len(dq)) == 0 :
            print('#%d YES' %(i+1))        
        else:
            print('#%d NO' %(i+1))


