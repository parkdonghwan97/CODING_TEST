


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();





def DFS(L,s,sum):
    global cnt 

    if L == k :  # DFS( 3 인경우 )

        if sum % m == 0 : # sum이 m으로나누어 떨어지는 경우 
            cnt+=1
    else:

         for i in range(s,n):
             DFS(L+1, i+1 , sum+a[i])       
        


if __name__=="__main__":
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    m = int(input())
    cnt = 0
    DFS(0,0,0)
    print(cnt)
# 5 3
# 2 4 5 8 12
# 6
