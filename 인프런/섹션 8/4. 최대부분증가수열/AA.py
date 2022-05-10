 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();


n= int(input())
m = list(map(int,input().split() ))

m.append(0,0) 

dy= [0] * (n+1)
dy[1] = 1
answer = 0 

for i in range(2,n+1):
    max = 0 
    for j in range(i-1, 0 , -1): 
        if m[i] > m[j]  and dy[j] > max:
            max = dy[j]
    dy[i] = max+1
    if answer <dy[i]:
        answer = dy[i]
print(answer)