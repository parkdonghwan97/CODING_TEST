# import sys
# sys.stdin = open('input.txt')






a = input()  
b = input()
c = {}
d = {}


for i in a:

    if i in c:
        c[i] +=1
    else:
        c[i] = 1

for i in b:

    if i in d:
        d[i] +=1
    else:
        d[i] = 1


if c == d :
    print('YES')
else:
    print("NO")