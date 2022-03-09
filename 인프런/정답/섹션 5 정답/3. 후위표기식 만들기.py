# import sys
# sys.stdin = open('input.txt')


x = input()  # 3+5*2/(7-2)



stack = []
answer = ''


# for i in range(len(x))  : 


#     if x[i].isdecimal == True:
#         stack.append(x[i])

    
#     else: # 숫자가 아닌경우 

#         if x[i] == '-' or x[i] == '+' :
#             stack.append(x[i])

#         elif x[i] =='/' or x[i] == '*':



# #stack = 3
    

# for i in stack:
#     print(i,end=' ')


for i in x : 

    if i.isdecimal(): # 10진수 숫자이면
        answer += i   # 더함
    else:

        if i == '(':
            stack.append(i)
        elif i =='/' or i=='*': # 곱하기나 나누기인경우
            #stack이 비어있지 않고, *, / 인경우
            while stack and (stack[-1]== '*' or stack[-1]=='/'):
                answer += stack.pop()
            stack.append(i)  # * / 처리완료

        elif i=='+' or i=='-':  # 더하기, 빼기인 경우

            #여는 괄호 전까지
            while stack and stack[-1] != '(':

                answer += stack.pop()
            stack.append(i)
        elif i ==')':

            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()

while stack:
    answer+=stack.pop()

print(answer)