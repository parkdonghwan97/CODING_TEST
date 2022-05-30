

# IV 터렛

# n = int(input())
 
# for i in range(n) :
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     r = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
#     R = [r1,r2,r]
#     m=max(R); R.remove(m)
#     print(-1 if (r==0 and r1==r2) else 1 if (r == r1+r2 or m==sum(R)) else 0 if (m > sum(R)) else 2)
'''
케이스 4가지 (두 원의 중점 사이 거리 r)
1. 두원이 일치하는 경우 => -1

r1 == r2

2. 두 원이 한 점에서 만나는 경우 (외접, 내접) => 1
(r== r1+r2)  or (r2 == (r+r1))

3. 두 원이 두점에서 만나는 경우 

4. 그마저도 아닌경우
'''

import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    
    # 두 원의 중심 사이의 거리
    dis = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    if dis == 0:    # 두 원의 중심이 같을 경우
        if r1 == r2: # 두 원의 크기가 같아 겹치는 경우
            print(-1)
        else:                     # 한 원이 다른 원 안에 들어가 있는 경우
            print(0)
    else:            # 두 원의 중심이 다를 경우
        if r1+r2 == dis or abs(r2-r1) == dis:
            print(1)
        elif ((abs(r1-r2) < dis) and (dis < r1+r2)):
            print(2)
        else:
            print(0)