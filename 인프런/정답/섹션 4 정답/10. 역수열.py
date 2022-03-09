# import sys


# n = int(input())


# a = list(map(int,input().split())) # 역수열


# x = [0] * n  # 0~ n-1 인덱스만 사용


# for i in range(n):
#     for j in range(n):

        
#         if a[i] == 0 and x[j] ==0:
#             x[j] = i+1
#             break


#         elif x[j] == 0 : # 빈자리
#             a[i] -=1 # 빈자리 발견하면 a[i]값을 하나 뺌

# for i in x:
#     print(i, end=' ')


n = int(input())

a = list(map(int,input().split()))

x = [0]*n 

for i in range(n):
    for j in range(n):
        
        
        if a[i] == 0 and x[j] == 0 : 

            x[j] = i + 1  # i는 인덱스 이므로 +1 
            break

        elif x[j] ==0 :
            a[i] -= 1

for i in x:
    print(i , end=' ')





