
import math
# math.lcm()  최소공배수  
# math.gcd()  최대공약수

a,b = map(int,input().split())


# 찾아보니 lcm은 파이썬 3.9부터 사용이 가능하다고 함.

# print(math.lcm(10,20))

print(math.gcd(a,b))


print( (a*b)// math.gcd(a,b)  )

# a,b의 최소공배수는 
# A*B를 최대공약수로 나눈 몫