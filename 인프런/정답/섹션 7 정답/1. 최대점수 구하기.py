 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();



def DFS(L,val,t):

    global answer
    if t > m:   # 제한시간 m 보다 시간이 큰경우 종료
        return

    if L == n:

        if val > answer:
            answer = val

    else:
        # 문제를 푸는경우
        DFS(L+1,  val+value[L] ,t + time[L]  )
        # 문제를 안푸는경우
        DFS(L+1,val,t)





n,m=map(int,input().split())

value = []
time = []

for i in range(n):
    a,b = map(int,input().split())
    value.append(a)
    time.append(b)
answer = -123
DFS(0,0,0)
print(answer)