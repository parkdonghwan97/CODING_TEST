


# import sys
# sys.stdin=open("input.txt", "r")
# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
import sys
def DFS(L,sum):
    
    if L == n :

        if sum*2 == tot:
            print("YES")
            sys.exit(0)
    
    else:
        DFS(L+1, sum + a[L])
        DFS(L+1, sum )





if __name__=='__main__':

    n = int(input())                          # 6
    a = list(map(int,input().split()))        # 1 3 5 6 7 10
    tot = sum(a)
    DFS(0, 0)
    print("NO") 