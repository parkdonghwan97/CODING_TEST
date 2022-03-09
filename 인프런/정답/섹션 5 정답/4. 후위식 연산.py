# import sys
# sys.stdin = open('input.txt')




a = input()

stack = [] 


for i in a:

    if i.isdecimal():
        stack.append(i)

    
    elif i =='+':
        x1 = stack.pop()
        x2 = stack.pop()
        stack.append(  int(x1)+int(x2) )

    elif i =='-':
        x1 = stack.pop()
        x2 = stack.pop()
        stack.append(int(x2)-int(x1))
    elif i =='*':
        x1 = stack.pop()
        x2 = stack.pop()
        stack.append(int(x1)*int(x2))
    elif i =='/':
        x1 = stack.pop()
        x2 = stack.pop()
        stack.append(int(x2)/int(x1))

print(stack[0])