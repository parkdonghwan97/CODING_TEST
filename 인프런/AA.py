 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();




def DFS(x,y):
    global cnt 

    if x==6 and y==6:
        cnt +=1 
    else:
        for i in range(4): # 4방향
            X = x + dx[i]
            Y = y + dy[i]

            # 범위 초과 아닌경우 , 벽이 아닌경우
            if 0<=X<=6 and 0<=Y<=6 and board[X][Y] ==0:
                board[X][Y] =1
                DFS(X,Y)
                board[X][Y] = 0






board  =  [ list(map(int,input().split())) for i in range(7)  ]
# 이제 이런문제 풀 때는, 12 시 3시 6시 9시 방향 기준으로 하자.
dx = [0,1,0,-1] 
dy = [-1,0,1,0]
cnt = 0 


board[0][0] = 1 
DFS(0,0) 
print(cnt)