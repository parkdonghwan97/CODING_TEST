 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();



def DFS(v):
    global cnt
    if v == n :  # v가 5가 된경우 
        cnt+=1

        # for i in path:
        #     print(*i)

    else:
        for i in range(1, n+1):  # 1부터 5까지  

            if g[v][i] ==1  and check[i]==0:    #  v에서 i로 방문했는지 체크

                check[i]=1
            
                # path.append(i) # 방문한경우 i를 path에 추가

                DFS(i)
                # path.pop()
                check[i]=0






n,m = map(int,input().split() ) 


g = [ [0]*(n+1) for i in range(n+1)  ]


check= [0] * (n+1)

for i in range(m):

    a,b = map(int,input().split())
    g[a][b]= 1 

cnt = 0

# 경로 저장 하는 변수
# path = []
# path.append(1) # 1번에서 출벌
check[1]=1
DFS(1)
print(cnt)

