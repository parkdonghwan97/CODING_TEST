


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();




import sys


def DFS(L,sum):
    
    if L == n  and sum ==f : # 종료지점
        print(*permu)
        sys.exit()
    
    else:

        for i in range(1, n+1): # 1부터 n까지
            if check[i] == 0:

                check[i] = 1 #  체크 1 
                permu[L] = i               # b = [1 3 3 1 ]
                                           # p = [ 1 2 3 4]  각 원소 값 곱함
                DFS(L+1, sum + (permu[L]*b[L]))
                check[i] = 0



n , f = map(int,input().split())
permu = [0] * n  # 순열 담을 변수
b = [1] * n      # 이항계수 저장      양 끝값은 1이기때문에 1로 초기화
check= [0] *(n+1) #순열만들때 중복방지용 체크 

for i in range(1,n):

    # ex) b = [1 1 1 1 ]   n이 4일때
    #      3C0 3C1 3C2 3C3 
    #    1x1 1x3  1x3  1x1   = [ 1 3 3 1 ]
    b[i] = (b[i-1] * (n-i)) //  i

# print(*b)
DFS(0,0)