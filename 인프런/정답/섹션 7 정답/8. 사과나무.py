 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();









# 홀수 
from collections import deque


n = int(input())

# 이동 좌표        상 하 좌 우 방향으로 
dx = [0,0,-1,1]
dy = [1,-1,0,0]

# 입력 받을 2차원 리스트 
a = [ list(map(int,input().split())) for i in range(n) ]  

# 자리 0 으로 초기화
ch = [ [0]*n for i in range(n)    ] 


sum = 0 

dq = deque()  
dq.append(   (n//2,n//2)  )  # 튜플형식으로 시작지점의 좌표 입력
# 중앙 지점 체크
ch[n//2][n//2]  = 1
sum+= a[n//2][n//2]


L = 0 # 시작점

while 1:
    if L== n//2 : # 2가되면 종료
        break 
    size = len(dq) #  size만큼 for문
    for i in range(size):
        tmp = dq.popleft()

        for j in range(4): # 상하 좌우 4방향
            x= tmp[0]+ dx[j]
            y= tmp[1]+ dy[j]
            
            # 방문 안한경우에만 sum 추가
            if ch[x][y] == 0:
                sum += a[x][y]
                
                #방문 한경우 ch 1로 변경
                ch[x][y] = 1
                dq.append((x,y))   # x y 좌표 추가 
    
    # 반복 끝나면
    L +=1 
print(sum)



