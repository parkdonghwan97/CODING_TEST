# import sys


n , m  = map(int,input().split())

n = list(map(int,str(n)))

# print(n)    [5, 2, 7, 6, 8, 2, 3]


stack = [] 
for i in  n : 

#  stack 이 비어있지 않고
#  m 이 0 보다 크고
#  stack의 맨 뒤에 있는 값이 i 보다 작은경우 

    while stack and m > 0 and stack[-1] < i :
        stack.pop() # 스택의 맨 뒤 제거 
        m-=1
    stack.append(i)

    '''
    i = 5
    스택은 비어있으므로 stack.append(5)
##########################################
    i = 2

    stack[-1] = 5 > i 면서 m>3 이므로
    m = 2 
    stack = [5, 2]
########################

    i = 7 
    stack[-1] = 2 < i 이므로 
    stack.append(7)
    
    
    '''
if m!=0:  # m이 0아닌경우 
    stack = stack[:-m]
answer = ''.join(map(str,stack))
print(answer)