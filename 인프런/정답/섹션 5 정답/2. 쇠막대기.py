# import sys
# sys.stdin = open('input.txt')


x = input()




#  (   <= 레이저 or  막대기 시작지점
# ( (   인경우    맨처음 ( 은 쇠막대기의 시작 지점

# ( ( ( 인 경우   1, 2 번째는 쇠막대기 시작 지점

#    ()    <- 인경우 레이저


# (를 스택에 넣고 )를 만나면 pop, len(stack)을 카운트함

stack = [] 

# (((()(()()))(())()))(()())
cnt = 0 
for i in range(len(x)):
    
    if x[i] == '(':
        stack.append('(')

    elif x[i] == ')':
        stack.pop()
        if x[i-1] == '(':  # 만약 앞의 값이 ( 인경우
            cnt+= len(stack)   # 레이저

        else: # 만약 앞의 값이 ) 인경우     
            cnt += 1 # 쇠막대기의 끝


print(cnt)

