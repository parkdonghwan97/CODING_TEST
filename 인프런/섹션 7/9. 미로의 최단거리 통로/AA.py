 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();



from collections import deque



# print(check)

# 상 하 좌 우
dx=[-1, 0, 1, 0]  
dy=[ 0,1,0,-1]


check = [[0] * 7  for _ in range(7)]
board= [ list(map(int,input().split()))  for i in range(7)]
# print(a)


dq =deque()
dq.append((0,0)) # 0,0 시작점 추가
board[0][0] = 1 

while dq:

    tmp = dq.popleft() # 0,0 좌표가 빠짐 
    for i in range(4): # 상하좌우 탐색
        x = tmp[0]+dx[i]
        y = tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y] == 0  :
        # if board[x][y] == 0  and 0<=x<=6 and 0<=y<=6: #벽이 아닌경우 , # 범위 초과 아닌경우
            board[x][y] = 1 # 방문처리
            check[x][y]= check[tmp[0]][tmp[1]] +1 # count? node 수 +1
            dq.append( (x,y)  )
# 방문 못한경우 -1
if check[6][6]==0:
    print(-1)
else:
    print(check[6][6])


            


