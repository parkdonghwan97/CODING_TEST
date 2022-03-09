# import sys
# sys.stdin = open('input.txt')

n,m = map(int,input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
lt,rt = min(a) , max(a)

def Count(d):
    cnt = 1
    endpoint = a[0] # 첫번째 마굿간
    for i in range(1,n):
        if a[i] - endpoint >= d :
            cnt+=1
            endpoint = a[i]
    return cnt 


# lt mid rt
answer = 0
while lt<=rt:
    mid = (lt+rt) //2
    if Count(mid)>=m:
        answer = mid
        lt = mid+1
    else:
        rt= mid-1
print(answer)


