


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();



def DFS(L,sum):
    
    global answer
    if sum > m :   # m보다 크면 종료
        return

    if L > answer:    # DFS(3) 보다 크면 종료 
        return
    
    if sum == m :  # m과 같다면
        
        if L < answer:
            answer = L 

    else:
        
        for i in a:   # a 만큼 돌려 
            DFS(L+1, sum +  i )






n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)  # 큰거부터 
m = int(input())
answer = 999
DFS(0,0)
print(answer)


# 3
# 1 2 5
# 15