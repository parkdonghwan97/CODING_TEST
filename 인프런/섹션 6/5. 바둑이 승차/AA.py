


# import sys
# sys.stdin=open("input.txt", "r")
# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# import sys
# def DFS(L,sum):
#     global x

#     if sum > c :
#         return


#     if L == n:  # 부분집합 완성 
        
#         if sum > x:  # 부분집합이 x보다 크면 x를 sum으로 바꿈 
#             x = sum
    

#     else:
#         DFS(L+1, sum+a[L])   # 1마리 무게를 추가
#         DFS(L+1, sum)    # 1마리 추가 X
    
# if __name__=='__main__':

#     c, n = map(int,input().split())
#     a = []
#     for i in range(n):
#         a.append(int(input()))
#     x = -1111
#     DFS(0,0)
#     print(x)

############## 시간초과남 .    ↓ short cut
def DFS(L,sum, tsum):
    global x
    # 추가 cut 
    if sum +  tot- tsum < x : 
        return 
    if sum > c :
        return


    if L == n:  # 부분집합 완성 
        
        if sum > x:  # 부분집합이 x보다 크면 x를 sum으로 바꿈 
            x = sum
    

    else:
        DFS(L+1, sum+a[L]  , tsum+a[L]  )   # 1마리 무게를 추가
        DFS(L+1, sum, tsum+a[L])    # 1마리 추가 X
    


if __name__=='__main__':

    c, n = map(int,input().split())
    a = []
    
    for i in range(n):
        a.append(int(input()))
    x = -1111
    tot = sum(a)
    DFS(0,0,0)
    print(x)