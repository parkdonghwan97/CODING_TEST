# import sys
# sys.stdin = open('input.txt')


from collections import deque



# n = int(input())
# a = list(map(int,input().split()))  # 2 4 5 1 3
# a= deque(a)
# answer=''
# cnt = 0 
# x = 0   # 비교할 변수를 담을 변수 


# while a:
#     if a[0] <= x :
#         a.popleft()
#         # a.pop(0)

#     if a[0] > x: 
#         x = a[0]
#         a.popleft()
#         # a.pop(0)
#         answer+='L'
#         cnt+=1
#          # 2


#     if a[-1] <=x:
#         a.pop()
#     if a[-1]> x:
#         x= a[-1]
#         a.pop()
#         answer+='R'
#         cnt+=1

# print(cnt)
# print(answer)        이렇ㄱ ㅔ 코드짜니 왼쪽에서 1번 오른쪽에서 1번씩 반복
#################### 실패  - 정답
n = int(input())
a = list(map(int,input().split()))  # 2 4 5 1 3

lt,rt = 0,n-1

x = 0 
answer = ''
cnt= 0 
tmp = [] 
while lt <= rt:
    if a [lt] > x:
        tmp.append((a[lt],'L'))
    if a[rt]>x:
        tmp.append((a[rt],'R'))
    tmp.sort()  

    if len(tmp) ==0 :  # 아무것도 안들어간경우
        break
    else:
        answer+= tmp[0][1]
        x = tmp[0][0]
        if tmp[0][1] =='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()

# print(cnt)
print(len(answer))
print(answer)








