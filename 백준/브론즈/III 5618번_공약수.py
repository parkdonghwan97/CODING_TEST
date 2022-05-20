

# III 5618번_ 공약수

# 풀긴했는데 코드가 너무 더럽다.

# from math import gcd
# n = int(input())

# if n ==2:
#     a,b = map(int,input().split())
#     gcd1 = gcd(a,b)

    

#     for i in range(1, gcd1+1):
#         if gcd1 % i == 0 :
#             print(i)

# else:
#     a,b,c = map(int,input().split())
    
#     gcd1 = gcd(a,b)
#     gcd2 = gcd(b,c)
#     gcd3 = gcd(gcd1,gcd2)

#     for i in range(1, gcd3+1):
#         if gcd3 % i == 0 :
#             print(i)


# 다른사람의 코드를 확인해보자.

# n = int(input())
# a = list(map(int,input().split()))
# for i in range(1,min(a)+1):
#     if n==2:
#         if a[0]%i==0 and a[1]%i ==0: 
#             print(i)
#     else:
#         if a[0]%i==0 and a[1]%i==0 and a[2]%i==0:
            # print(i)

# 굳이 gcd쓰지않고 이렇게 푸는것도 조흔 방법인듯.


# 시간이  72ms밖에 안걸린 코드

from math import sqrt, gcd

def f(n):
    l = [] 
    for i in range(1,int(sqrt(n))+1):
        if not n %i :  # n % i 가 0이 아닌경우
            l.append(i)

            if (i**2) !=n:
                l.append(n//i)

    l.sort()
    return l 

a = int(input())
l = list(map(int, input().split()))
g = l[0]

for x in range(a-1):
    g = gcd(g, l[x+1])

r = f(g)
for e in r:
    print(e)