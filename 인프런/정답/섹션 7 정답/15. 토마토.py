 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();





from collections import deque
dx = [0,1,0,-1]
dy = [-1,0,1,0]

n,m = map(int,input().split())

dq = deque()
cnt = 0 
board =[ list(map(int,input().split()) )  for i in range(m)]
ch = [[0]*n for i in range(m)] # 


# n,m바뀐거 주의

for i in range(m):
    for j in range(n):

        # 1의 위치에서 BFS 뻗음
        if board[i][j] ==1: 
            dq.append([i,j]) 

while dq:
    tmp = dq.popleft()
    for i in range(4):
        X = dx[i]+ tmp[0]
        Y = dy[i]+ tmp[1]
        
        # 행은 m이다  다시,,
        if 0<=X<m and 0<=Y<n and board[X][Y] == 0 :  # 범위 초과하지 않고 빈공간인경우
            board[X][Y] = 1   # 1로 변경
            ch[X][Y] = ch[tmp[0] ][tmp[1]]  + 1 # 현재 지점 +1

            dq.append([X,Y])  # X Y 큐에 추가 


flag = 1 


for i in range(m):
    for j in range(n):

        # 안익은 토마토가 없는 경우
        if board[i][j] ==0: 
            flag = 0   # flag를 0으로 변경 

answer = 0 


if flag ==1:
    for i in range(m):
        for j in range(n):
            if ch[i][j] > answer:
                answer = ch[i][j]  # 최대 날짜 값 
    print(answer)
else:
    print(-1)

