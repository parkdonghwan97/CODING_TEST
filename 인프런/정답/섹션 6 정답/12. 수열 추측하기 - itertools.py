


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();





import itertools
import sys 
n, f =  map(int,input().split())
a = [i for i in range(1,n+1)]

b = [1] * n 
cnt = 0
for i in range(1,n):
    b[i] = b[i-1] *(n-i) //i   # 이항계수 


for i in itertools.permutations(a,n):
    sum = 0 

    for L, x in enumerate(i):
        # print(L,x)    # 인덱스 , 값
        sum += (x *b[L])
    
    if sum ==f:
        print(*i)
        #sys.exit()
        break
  
