

# I 1356번_유진수

# 어떤 수를 10진수로 표현한 뒤 그 수를 두 부분으로 나눴을 때, 
# 앞부분 자리수의 곱과 뒷부분 자리수의 곱이 같을 때

n = input()
Flag = False 
for i in range(1,len(n)):
    x1,x2 = n[:i], n[i:]
    a,b = 1 ,1
    for x in x1:
        a *= int(x)
    for x in x2:
        b*= int(x)
    if a == b :
        Flag = True 
        break 

if Flag:    
    print("YES")
else:
    print("NO")

# 다른 코드

def UJS(x):
    ans = 1
    for n in x : 
        ans*=n
    return ans  
a =list(map(int,input()))

n = len(a)
ans = 'NO'

for i in range(1,n):
    L1,L2 = a[:i],a[i:]
    if UJS(L1)==UJS(L2) :
        ans = 'YES'
print(ans)