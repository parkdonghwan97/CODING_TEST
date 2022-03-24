 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();



def DFS(L, sum):
    global answer 
    if L == k:  # 종료

        if 0< sum <= s:
            answer.add(sum)


    else:
        DFS(L+1, sum+ a[L]) # 왼쪽에  추가 
        DFS(L+1, sum-a[L])  # 오른쪽에 추가
        DFS(L+1,sum)        # 사용 x 







k = int(input())
a = list(map(int,input().split()))

s= sum(a)
answer=set() # 중복제거
DFS(0,0)

print(s  -  len(answer))