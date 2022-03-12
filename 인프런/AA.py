


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();

def DFS(L):
    
    global cnt
    if L == m: # 중복순열 완성 
        print(*answer)
        
        cnt+=1
            
    
    else:

        for i in range(1,n+1): # 1~ n까지
            answer[L] =i
            DFS(L+1)










if __name__=='__main__':
    n,m = map(int,input().split())
    cnt = 0
    answer = [0] * m 
    DFS(0)
    print(cnt)
    
