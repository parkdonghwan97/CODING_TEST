# import sys
# sys.stdin = open('input.txt')

n = int(input())  # n은 홀수 
a = list()
for i in range(n):
    a.append(list(map(int,input().split())))
tot = 0
# print(a) [[10, 13, 10, 12, 15], [12, 39, 30, 23, 11], [11, 25, 50, 53, 15], [19, 27, 29, 37, 27], [19, 13, 30, 13, 19]]
'''
5x5인경우
10 13 10 12 15    1
12 39 30 23 11    3
11 25 50 53 15    5
19 27 29 37 27    3
19 13 30 13 19    1
'''
e = s  = n // 2 


for i in range(n):

    for j in range(s, e+1):
        tot += a[i][j]
    if i < n//2:   
        s -=1
        e +=1
    else:   
        s+=1
        e-=1
print(tot)



