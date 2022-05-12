
n = (input())


f = int(input())

a = int( n[:-2] + '00' )
# print(a)

while 1:   # 나누어 떨어질 때 까지 더함
    if a%f ==0:
        break 
    a+=1 
print( str(a)[-2:])