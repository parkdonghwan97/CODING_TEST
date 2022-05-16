


# N운동시간 m 맥박 M최대맥박, T맥박증가량, R휴식하는경우 감소

# 운동 긑내지 못하면 m+T > N

N,m,M,T,R = map(int,input().split())
n=m
time = 0 
tot = 0 
exercise = 0 

if m+T >M:
    print(-1)
else:

    while exercise< N:
        if n+T <=M:
            n+=T
            exercise+=1 
            tot+=1
        else:
            n=max(n-R,m)
            tot+=1 
    print(tot)