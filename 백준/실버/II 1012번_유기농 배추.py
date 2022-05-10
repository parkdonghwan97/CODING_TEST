import sys
sys.setrecursionlimit(100000)

answer = []
def DFS(x,y):
    global cnt
    # 12 3 6 9 시 
    dx = [ 0,1,0,-1 ]
    dy = [ 1,0,-1,0 ]

    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]

        if 0<=X<a and 0<=Y<b :
            if board[Y][X] == 1:
                board[Y][X] = -1  # -1로 체크
                
                DFS(X,Y)

T = int(input())

for i in range(T):
    a,b,k =map(int,input().split()) # 가로 세로 개수
    
    board = [ [0]*a for i in range(b) ]
    cnt = 0 

    for j in range(k): # 배추가 있는 칸 1로 변경 
        tmp1, tmp2 = map(int,input().split())      # x y 바꿔야댐;;
        board[tmp2][tmp1] = 1    
    
    
    for q in range(a):
        for w in range(b):
            if board[w][q] == 1 : 
                DFS(q,w)
                cnt+=1
    answer.append(cnt)
for i in answer:
    print(i)