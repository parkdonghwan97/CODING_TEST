# import sys
# sys.stdin = open('input.txt')

n =int(input())
a = [list(map(int,input().split()))  for i in range(n) ]

m = int(input())
for i in range(m):
    h,t,k = map(int,input().split())  #  행 방향 k번이동

    # 왼쪽 or 오른쪽
    if t== 0 : # 0 - 왼쪽 
        for i in range(k):                # 2 0 3 
            a[h-1].append(a[h-1].pop(0))     #0번값 빼기 
    else:
        for i in range(k):
            # a[h-1].insert(0, a[h-1][-1]  ) # 맨뒤 자리를 맨앞으러 @@@@
            a[h-1].insert(0, a[h-1].pop()  )

# for i in a:
    # print(i) # [23, 11, 12, 39, 30]
'''
5
3
1
3
5
'''
s, e = 0,n-1
tot = 0
for i in range(n):
    for j in range(s,e+1):
        tot += a[i][j]
    if i  < n //2 :
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(tot)





