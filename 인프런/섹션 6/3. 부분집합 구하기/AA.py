from ntpath import join
import sys
# import sys
# sys.stdin=open("input.txt", "r")
# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 


def DFS(v):

    if v > n:

        for i in range(1, n+1):
            if a[i]==1:
                print(i,end=' ')
        print()
        return

    else:
        a[v] = 1
        DFS(v+1)
        a[v] = 0 
        DFS(v+1)

if __name__=='__main__':

    n = int(input())
    a=[0]*(n+1)
    DFS(1)