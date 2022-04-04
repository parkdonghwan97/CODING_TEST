 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();




# BFS
from collections import deque


n = int(input())
board = [list(map(int,input().split() ))  for i in range(n)]

# 상하좌우 아닌 팔각임
# dx = [0,1,0,-1]
# dy = [-1,0,1,0]

# 12시 기준 팔방 [북 북동 동 남동 남 남서 서 북서]
dx = [0 ,1 ,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]

dq = deque()
answer = []
for i in range(n):
    for j in range(n):
        if board[i][j]== 1:
            board[i][j] = 0
            dq.append([i,j]  )
            while dq:
                
                cnt = 0
                tmp  = dq.popleft()
                for a in range(8):
                    X = dx[a] + tmp[0]
                    Y = dy[a] + tmp[1]
                    if 0<=X<n and 0<=Y<n and board[X][Y] ==1:
                        board[X][Y] = 0 
                        dq.append([X,Y])
                        cnt+=1
            answer.append(cnt)        
print(len(answer))


