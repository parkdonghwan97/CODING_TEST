# import sys
# sys.stdin = open('input.txt')

# n,m = map(int,input().split())

# a = list(map(int,input().split()))

# # print(a) [90, 50, 70, 100, 60]

# a.sort()  #50 60 70 90 100

# cnt = 0 


# '''
# 맨뒤 + i번째가 140보다 크면 맨뒤 제거  cnt + 1
# 맨뒤 + i번째가 140 이하인 경우  둘다 제거 cnt++1
# '''

# while a :
#     if a[0] + a[-1] > m :  #50 + 100   > 140
#         a.pop(-1)
#         cnt += 1
#         # tmp += 1 
#     else:
#         a.pop(0)
#         a.pop(-1)
#         cnt+=1

#     if len(a) == 1:  # 1명이 남은경우 
#         cnt+=1
#         break
# print(cnt)

from collections import deque

n,m = map(int,input().split())

a = list(map(int,input().split()))
a.sort()
a =  deque(a)
cnt=0
while a:
    if a[0] + a[-1] > m:
        cnt+=1
        a.pop()
    else:
        cnt+=1
        a.pop()
        a.popleft()  # 맨 앞에거 하나제거 이게 더 좋다고 함.

    if len(a) == 1:
        cnt+=1
        break
print(cnt)