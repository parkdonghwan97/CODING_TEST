


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();


# def DFS(L):
    

#     if sum(a) == 2:
#         return 
    





# if __name__ =='__main__':
#     n,m = map(int,input().split())
#     a = [0]  * (n+1)

from itertools import permutations

n,m = map(int,input().split())
a = []
for i in range(1,n+1):
    a.append(i)

cnt = 0
for i in list(permutations(a,m)):
    cnt+=1
    print(*i)
print(cnt)