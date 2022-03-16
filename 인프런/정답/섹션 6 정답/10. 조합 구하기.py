


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();



def DFS(L,sum):
    global cnt
    if L == m : 
        print(*answer)
        cnt+=1
    else:
        
        for i in range(sum , n+1 ): 

        # if check[L] == 0 :
            # check[L] = 1
            answer[L] = i
            DFS(L+1, i+1 )
            # 다음 가지는 Sum+1 부터
            # check[L] = 0




n,m = map(int,input().split())
# check= [0] *(n+1)
answer=[0] * m
cnt = 0 
DFS(0,1)
print(cnt)






# n,m = map(int,input().split())
# from itertools import combinations
# a = []
# for i in range(1,n+1):
#     a.append(i)
# # print(a) # 1 2 3 4 

# cnt = 0
# for i in combinations(a,m) :
#     print(*i)
#     cnt+=1
# print(cnt)
