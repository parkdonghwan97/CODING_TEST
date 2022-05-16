
# N 세로, M 가로
from re import L


N,M = map(int,input().split())

cnt = 0
for i in range(N):
    a = input()
    if  a.count('X') == 0 :
        cnt+=1 
        
print(cnt)
