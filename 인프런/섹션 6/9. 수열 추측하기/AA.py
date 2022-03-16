


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();

def DFS(L,sum):
    if L == n and sum == f :# 답찾은경우
        print(*permu)

    else:
        for i in range(1,n+1) : # 1부터 n까지
            
            if check[i] == 0 : 
                check[i] = 1
                permu[L] = i 

                DFS(L+1, sum + permu[L] * bi[L] ) # sum에 permu * binary 값 더함
                check[i] = 0




n, f = map(int,input().split())

permu = [0] * n 
bi = [1] * n   # 이항계수 처음과 마지막항은 1이기 떄문에 1로 초기화
check = [0] *(n+1)
for i in range(1,n) :  # 1부터 n-1 까지 이항계수 구하면 되니까
    bi[i] = (bi[i-1] * (n-1))//i 

DFS(0,0)