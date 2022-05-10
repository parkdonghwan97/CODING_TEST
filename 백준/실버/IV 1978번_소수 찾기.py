
n = int(input())
answer = 0 
A = list(map(int,input().split())) # 1 3 5 7 
for i in A :
    
    cnt = 0 
    
    for x in range(1,i+1): # 1부터 a까지 나누기
        if i % x == 0:
            cnt+=1
    if cnt == 2:
        answer+=1


print(answer)