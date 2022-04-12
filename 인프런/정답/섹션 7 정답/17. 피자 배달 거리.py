 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();


# 0411
def DFS(L,s):
    global answer
    if L ==m :    # 살아남는 피자집
        # print(*X)
        sum = 0 
        for i in range(len(house)) : # 0~  집 개수만큼 
            x1= house[i][0]     
            y1=house[i][1]        
            distance = 9999
            for j in X:  # 피자집 인덱스 
                x2 = pizza[j][0]
                y2 =    pizza[j][1]

                distance = min(distance, abs(x1-x2) + abs(y1-y2))
            sum += distance
        if sum < answer :
            answer = sum  

    else:
        for i in range(s, len(pizza)) :#  0 ~ 피자집개수만큼
            X[L] = i 
            DFS(L+1 ,i+1)


# 격자크기, 살아남는 피자집
n,m = map(int,input().split())

board = [ list(map(int,input().split())) for i in range(n) ]
house = []
pizza = []
answer = 9999

X = [0] * m  # 피자집 조합 0 초기화 

for i in range(n):
    for j in range(n):
        if board[i][j] ==1:
            house.append( [i,j] )  # 집 주소 추가
        elif board[i][j] ==2: 
            pizza.append([i,j])
DFS(0,0)
print(answer)