 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();




# # 무방향 그래프
# n,m = map(int,input().split())
# g = [ [0]*(n+1) for i in range(n+1)  ]


# for i in range(1,n+1):

#     for j in range(1, n+1):
#         print(g[i][j], end=' ')
#     print()



# 무방향 그래프
n,m = map(int,input().split())
g = [ [0]*(n+1) for i in range(n+1)  ]

# 간선 정보
for i in range(m):
    a,b = map(int,input().split())  # 하나의 간선 정보 
    g[a][b], g[b][a]= 1,1


for i in range(1,n+1):

    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()





