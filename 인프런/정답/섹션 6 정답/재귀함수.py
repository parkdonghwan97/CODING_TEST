# import sys
# sys.stdin = open('input.txt')


# 재귀함수와 스택 

def DFS(x):
    if x>0:
        
        DFS(x-1)
        print(x, end=' ')


if __name__=='__main__':
    n = int(input())
    DFS(n)




# 재귀함수 사용할 때마다 Stack에 DFS()함수가 쌓임


# stack = [ DFS(3), DFS(2), DFS(1) DFS(0) ]   DFS(0)에서 함수 종료 .
# stack = [ DFS(3), DFS(2), DFS(1) ] 
# stack = [ DFS(3), DFS(2)]
# stack = [ DFS(3) ]
# stack = [ ]







