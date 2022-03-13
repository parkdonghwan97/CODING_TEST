


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();

def DFS(L,sum):
    global answer

    if L > answer:
        return

    if sum > m :
        return

    if sum == m:
        if L < answer:
            answer = L
        
    
    else:
        for i in a:
            DFS(L+1 ,sum+i  )
        # for i in range(n):
        #     DFS(L+1,sum+a[i])
            

if __name__=='__main__':
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input()) 
    answer = 999  # 최소값 
    a.sort(reverse=True)  # 큰동전부터 셀것.
    DFS(0,0)
    print(answer)
    