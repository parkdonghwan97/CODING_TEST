# import sys
# sys.stdin = open('input.txt')



def DFS(len):

    # CUT 
    if dy[len] !=0 : #이미 있는 경우
        return dy[len]  


    if len == 1  or len ==2  :   # 1m 2m일때 각각 1, 2  
        return(len)
    else:
        dy[len] = DFS(len-1) + DFS(len-2)   #  DFS(7) = DFS(6) + DFS(5)
        return dy[len]



n = int(input())
dy = [0]*(n+1) # 1번 ~ n까지 사용하기위함

print(DFS(n))