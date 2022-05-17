


# III 1267번_핸드폰 요금
def y(n):
    x = 0
    while True:
        

        if n < 30 :
            x += 10
            break 
        else:
            x+=10
            n-=30
    return(x)
            
def m(n):
    x = 0
    while True:
        

        if n < 60 :
            x += 15
            break 
        else:
            x+=15
            n-=60
    return(x)

n = int(input())
a = list(map(int,input().split()))

tmp1 = [] 
tmp2 = []
for i in a:
    tmp1.append(y(i))
    tmp2.append(m(i))
# print(tmp1, tmp2)
YS = sum(tmp1)
MS = sum(tmp2)

if YS < MS:
    print('Y', YS)
elif YS > MS:
    print('M', MS)
else:
    print('Y', 'M', MS)
     

# 다른 코드
# N = int(input())
# M = list(map(int, input().split()))
# YS = 0
# MS = 0
# for i in range(N):
#     YS += (M[i]//30 +1) * 10
#     MS += (M[i]//60 +1) * 15

# if YS < MS:
#     print('Y', YS)
# elif YS > MS:
#     print('M', MS)
# else:
#     print('Y', 'M', MS)