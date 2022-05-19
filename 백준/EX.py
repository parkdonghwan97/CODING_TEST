

# III 5618번_ 공약수


from math import gcd
n = int(input())

if n ==2:
    a,b = map(int,input().split())
    gcd1 = gcd(a,b)
    x= 1
    for i in range(gcd1):
        if i % x == 0 :
            print(x)
        else:
            x+=1
        


else:
    a,b,c = map(int,input().split())
    
    gcd1 = gcd(a,b)
    gcd2 = gcd(b,c)