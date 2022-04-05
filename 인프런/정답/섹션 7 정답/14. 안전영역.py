 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();



def DFS(x,y,h):
    ch[x][y]= 1
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if 0<=X<n and 0<=Y<n and ch[X][Y]==0 and board[X][Y] > h:
            DFS(X,Y,h)
n = int(input())
board = [list(map(int,input().split()))for i in range(n) ]
answer = 0
cnt=0           # 이거 설정 안하면 안되더라구요
dx = [0,1,0,-1]
dy = [-1,0,1,0]
for x in range(100):
    ch = [ [0]*n for i in range(n) ]  # 0  초기화
    cnt =0
    for i in range(n):
        for j in range(n):
            #0~100 사이 h값 보다 높은경우
            if ch[i][j]==0 and board[i][j]> x:
                cnt+=1
                DFS(i,j,x)
    answer = max(answer,cnt)
    # cut 해줘야댐 4,5 번 오류

    # if cnt ==0:

    #     break



print(answer)