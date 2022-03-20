 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();




# 인접행렬

n,m = map(int,input().split())  # 노드, 엣지

# 그래프 초기화

g = [ [0] *(n+1) for i in range(n+1) ]

#  노드, 엣지, 가중치 입력받기
for i in range(m):
    a,b,c = map(int,input().split()) # 노드, 엣지, 가중치
    
    for j in range(n):
        g[a][b] = c



# 그래프 출력 
for i in range(1,n+1):
    for j in range(1,n+1):
        print(g[i][j], end=' ')
    print()


