import sys
# import sys
# sys.stdin=open("input.txt", "r")
input = sys.stdin.readline       # 입력 량이 많을 때 사용. 

# s = input().rstrip(); 


def DFS(L):
    if L == m : # 하나의 중복순열 완성

        for i in range(m):
            print(res[i] ,end=' ')
        print()
        global cnt
        cnt+=1 
        return 
    
    
    
    
    else:
        for i in range(1,n+1) : # 1 부터 n 까지
            res[L] = i
            DFS(L+1)


if __name__=="__main__":
    n,m = map(int,input().split())   # 3,  2 
    res = [0] * m 
    cnt= 0
    DFS(0)
    print(cnt)
    
