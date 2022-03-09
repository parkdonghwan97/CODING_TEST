# import sys
# sys.stdin = open('input.txt')



# def DFS(L, sum):  

#     global result

#     if sum > c :
#         return


#     if L == n : 

#         if sum >result :
#             result= sum
#     else:
#         DFS(L+1,sum+a[L])
#         DFS(L+1,sum)




# if __name__ =="__main__":
#     c,n = map(int,input().split())  # 무게 제한, 
#     a=[0] * n  # 바둑이의 무게를 a에 저장 
#     result = -9999   # 최종값을 작은값으로 저장하고 계속 바꿔줌
#     for i in range(n):
#         a[i] = int(input())
#     DFS(0,0)
#     print(result)


################################# 타임 리밋.
# 전체 무게에서  L 까지 가지친 바둑이 무게를 합친 값과 비교해서 

def DFS(L, sum  , tsum ):  

    global result

    # total -tsum :나머지 바둑이 값. 

    if sum + (total - tsum) < result :
        return


    if sum > c :
        return


    if L == n : 

        if sum >result :
            result= sum
    else:
        DFS(L+1,sum+a[L],   tsum+a[L] )
        DFS(L+1,sum ,   tsum+a[L])




if __name__ =="__main__":
    c,n = map(int,input().split())  # 무게 제한, 
    a=[0] * n  # 바둑이의 무게를 a에 저장 
    result = -9999   # 최종값을 작은값으로 저장하고 계속 바꿔줌
    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    DFS(0,0,0)
    print(result)