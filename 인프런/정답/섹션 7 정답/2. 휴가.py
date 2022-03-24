 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();


# import sys
# sys.stdin = open('input.txt')

def DFS(L, sum ):
    global answer

    if L == n+1:  # 날짜 +1일
        if sum > answer:
            answer =sum

    else:
        if L+T[L] <= n+1 : # 현재지점 + 걸리는 날짜 가  n+1 이하인경우 진행
            DFS(L+T[L],sum + P[L]) # 상담날짜 더하고 sum에 추가

        DFS(L+1 ,sum) # 상담 안하면 바로 다음날,



n = int(input())
T =[]
P = []
for i in range(n):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)
T.insert(0,0)
P.insert(0,0)
answer = -999
DFS(1,0)
print(answer )