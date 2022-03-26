 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();




def DFS(L,sum):
    global cnt
    # cut
    if sum > T:
        return

    if L ==  k :

        if sum ==T:
            cnt+=1

        


    else:
        for i in range(n[L]+1):
            DFS(L+1,sum+p[L]*i)
  #      for i in range(n):   여기 다시 볼것

   #         DFS(L+1, sum +   i* )
            



T = int(input()) # 금액
k = int(input()) # 동전개수


p,n= [],[]
for i in range(k):
    a,b = map(int,input().split())   # 5-3    10-2   1-5  n원짜리동전-개수

    p.append(a)
    n.append(b)
cnt = 0 

DFS(0,0)
print(cnt)



