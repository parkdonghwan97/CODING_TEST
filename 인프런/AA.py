


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();


def DFS(L):
    
    global cnt

    if L == m :
        
        print(*answer[0:2])
        cnt+=1
    
    else:
        for i in range(1,n+1):
            if check[i] == 0 : 
                check[i] = 1 
                answer[L] = i
                DFS(L+1)
                check[i] = 0 




if __name__ =='__main__':
    n,m = map(int,input().split())
    answer = [0]  * n 
    check= [0] * (n+1)
    cnt = 0 
    DFS(0)
    print(cnt)




# DFS 안쓰면 이런 방법도 있기는 함미다. ㅎㅎ.
# from itertools import permutations

# n,m = map(int,input().split())
# a = []
# for i in range(1,n+1):
#     a.append(i)

# cnt = 0
# for i in list(permutations(a,m)):
#     cnt+=1
#     print(*i)
# print(cnt)