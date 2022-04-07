 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();




def DFS(x,y):
    ch[x][y] =  1  

    if x ==0:
        print(y) # 열번호 출력
    else:
        # 왼쪽 오른쪽 위 순서로 확인 
        # 체크가 안되어있는 경우 사다리(1)인 경우
        if y-1 >=0 and board[x][y-1] ==1 and ch[x][y-1] ==0:
            DFS(x,y-1)
        elif y+1 <10 and board[x][y+1] ==1 and ch[x][y+1] ==0:
            DFS(x,y+1)
        # elif x-1 >=0 and board[x-1][y] ==1 and ch[x-1][y] ==0:
        #     DFS(x-1,y)
        else:
            DFS(x-1,y)

# 마지막 행을 확인하면 시간 단축 가능


ch = [[0]*10 for i in range(10) ]
board = [list(map(int,input().split())) for i in range(10)]


for y in range(10): # 열 
    

    if board[9][y] == 2  :# 마지막 행 값이 2인경우 거기서 부터 DFS 시작
        DFS(9,y)