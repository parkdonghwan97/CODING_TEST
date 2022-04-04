 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();



from collections import deque
# dx=[0,1,0,-1]
# dy=[-1,0,1,0]

# n = int(input())
# # ch = [[0]*n for i in range(n)]
# board = [list(map(int,input().split())) for i in range(n)]

# MIN = 9999
# MAX = -9999

# dq = deque()
# cnt = 0 
# for i in range(n):
#     for j in range(n):
        
#         if board[i][j] < MIN:
#             MIN = board[i][j]
#             sx = i
#             sy = j
#             dq.append([i,j])

#         elif  board[i][j] >MAX:
#             MAX = board[i][j]
#             ex=i
#             ey=j
        
# while dq:
#     tmp = dq.popleft()

#             #
#     if tmp[0] == ex and tmp[1]==ey:            
#         cnt+=1
                

#     for a in range(4):
#         X = dx[a]+tmp[0]
#         Y = dy[a]+ tmp[1]

#         if 0<=X<n and 0<=Y<n and board[X][Y] > board[tmp[0]][tmp[1]]   :
#                     # board[X][Y] = 0
#             dq.append([X,Y])
                       
# print(cnt)




# dx=[0,1,0,-1]
# dy=[-1,0,1,0]

# n = int(input())
# board = [ [0]*n for i in range(n) ]
# dq = deque()
# MAX = -999
# MIN = 999
# cnt = 0 

# for i in range(n):  # 한 줄씩 입력 받기 
#     tmp = list(map(int,input().split()))
#     for j in range(n):
#         board[i][j] = tmp[j]

#         if tmp[j] < MIN :
#             MIN = tmp[j]
#             sx =i 
#             sy =j 
#             dq.append([sx,sy])
#         elif tmp[j]>MAX:
#             MAX = tmp[j]
#             ex = i 
#             ey = j 

# while dq:
#     tmp = dq.popleft()

#             #
#     if tmp[0] == ex and tmp[1]==ey:            
#         cnt+=1
                

#     for a in range(4):
#         X = dx[a]+tmp[0]
#         Y = dy[a]+ tmp[1]

#         if 0<=X<n and 0<=Y<n and board[X][Y] > board[tmp[0]][tmp[1]]   :
#                     # board[X][Y] = 0
#             dq.append([X,Y])
                       
# print(cnt)

def DFS(x,y):
    global cnt
    if x ==ex and y==ey : 
        cnt+=1
    else:
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]

            if 0<=X<n and 0<=Y<n and board[X][Y] > board[x][y] :# 기존 값보다 큰경우
                
                DFS(X,Y)
                

    
dx = [0,1,0,-1]
dy = [-1,0,1,0]
n = int(input())
board = [list(map(int,input().split())) for i in range(n)]
# board = [ [0]*n for i in range(n) ]

MAX = -9999
MIN= 9999

for i in range(n):
    # tmp = list(map(int,input().split()))
    for j in range(n):
        if board[i][j] < MIN:
            MIN = board[i][j]
            sx = i
            sy=  j
        if board[i][j] > MAX:
            MAX = board[i][j]
            ex = i
            ey=  j
        # if tmp[j] < MIN :
        #     MIN = tmp[j]
        #     sx =i
        #     sy = j  
        # if tmp[j] > MAX :
        #     MAX = tmp[j]
        #     ex = i 
        #     ey = j 
        
cnt = 0
DFS(sx,sy)
print(cnt)



       