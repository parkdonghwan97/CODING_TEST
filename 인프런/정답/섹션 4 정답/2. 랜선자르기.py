# import sys
# sys.stdin = open('input.txt')

k,n=map(int,input().split())
a = []
maxvalue = 0 
for i in range(k):
    tmp = int(input())
    a.append(tmp)
    maxvalue = max(maxvalue, tmp)  # 이전값, 입력값 중에 큰값

# lt   mid   rt
lt , rt  = 1 ,  maxvalue

answer = 0 
while lt<=rt:
    mid = (rt+lt) // 2
    cnt = 0 

    for i in a:
        cnt +=( i//mid)

    if cnt >= n :
        answer = mid
        lt = mid +1

    elif cnt < n :
        rt= mid - 1   
    
    
    # if lt>rt:
    #     break
print(answer)




