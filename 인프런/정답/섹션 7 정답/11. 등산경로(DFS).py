 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();


## DFS  
# def DFS( x,y):
#     global cnt
#     cnt+=1
#     dx = [0,1,0,-1]
#     dy = [-1,0,1,0]
#     board[x][y]=0

#     for i in range(4):   # 상하자우 4번 
#         X = x+dx[i]
#         Y = y+dy[i]

#         if 0<=X<n and 0<=Y<n  and board[X][Y] == 1  : # 범위초과 x 방문 안한경우
#             DFS(X,Y)



# n = int(input())
# board  = [list(map(int,input())) for i in range(n)]
# answer = []
# for i in range(n):
#     for j in range(n):

#         if board[i][j]== 1:
#             cnt  = 0 
#             DFS(i,j)
#             answer.append(cnt)
# answer.sort()
# print(len(answer))
# print(*answer)

#DFS

def DFS(x,y):
    global cnt
    if x ==ex and y==ey : 
        cnt+=1
    else:
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]

            if 0<=X<n and 0<=Y<n and board[X][Y] > board[x][y] :# 기존 값보다 큰경우
                ch[X][Y]=1 # 1변경 DFS 후 다시 0
                DFS(X,Y)
                ch[X][Y] = 0

    
dx = [0,1,0,-1]
dy = [-1,0,1,0]
n = int(input())
# board = [list(map(int,input().split())) for i in range(n)]
board = [ [0]*n for i in range(n) ]
ch = [ [0]*n for i in range(n) ]
MAX = -9999
MIN= 9999

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if tmp[j] < MIN :
            MIN = tmp[j]
            sx =i
            sy = j  
        if tmp[j] > MAX :
            MAX = tmp[j]
            ex = i 
            ey = j 
        board[i][j] = tmp[j]    
ch[sx][sy] = 1  
cnt = 0
DFS(sx,sy)
print(cnt)






