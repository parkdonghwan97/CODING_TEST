# import sys
# sys.stdin = open('input.txt')


# 100점 뜨긴하는데 수정된 내용은 강의 영상못봤씀니다 설명좀여 ^^;
n,m = map(int,input().split())    
a = list(map(int,input().split()))

def Count(c):
    cnt = 1   # DVD1장
    tot = 0   # DVD노래합
    for i in a:
        if tot + i  > c :  # 용량 초과인경우 
            cnt+=1 
            tot = i 
        else:  # 초과 되지 않은 경우
            tot += i 
    return cnt

# lt  mid   rt 
lt , rt = 1, sum(a)
answer= 0 
while lt<=rt:
    mid = (lt+rt) // 2   
    cnt = 0
    tot = 0  
    if  Count(mid) <= m : # m보다 작거나 같은경우 
        answer = mid 
        rt = mid-1
    else:
        lt = mid+1
print(answer)
