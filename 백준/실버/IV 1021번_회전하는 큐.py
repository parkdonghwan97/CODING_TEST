

# IV 1021번_회전하는 큐

# deque -  rotate(1)    rotate(-1) 하는 법만 알면 금방 품

'''
1번째 원소 뽑음 a1 a2 a3 ak => a2 a3 ak-1 ak
왼쪽으로 한칸 이동  a1 a2 a3 ak => a2 a3 ak a1
오른쪽으로 한칸이동 a1 a2 a3 ak => ak a1 a2 ak-1
'''

from collections import deque as dq

n,m = map(int,input().split())

a = dq( [i for i in range(1,n+1)])
cnt = 0 

idx = list(map(int,input().split()))

for i in idx:
    while 1: 
        if a[0] ==i :
            a.popleft()
            break
        else:
            if a.index(i) <= len(a)//2:
                a.rotate(-1) # 이걸 몰랐냉;;
                cnt+=1
            else:
                a.rotate(1)
                cnt+=1
print(cnt)