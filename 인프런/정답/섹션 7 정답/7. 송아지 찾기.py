 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();











# 현수 위치, 송아지 위치 좌표는 1~ 10000
from collections import deque


s,e = map(int,input().split())

r = 10000 # 범위 10000
distance = [0] *(r+1)
check = [0] *(r+1)

check[s] = 1 # s출발 = 1
distance[s] = 0 

dq = deque()
dq.append(s)
while dq: # dq가 비어있으면 종료
    now = dq.popleft() # 맨 왼쪽 뽑아서 탐색  

    if now ==e : # 목표지점인 경우
        print(distance[e]) 


    for i  in(now-1, now+1,now+5):
        if 0<i<=r  and check[i]==0 :  # 범위에 있고 방문 안한경우
            dq.append(i) # 큐에 i 추가
            check[i] = 1  #  방문했으니 1로 변경
            # distance[i] = now+1 
            distance[i] = distance[now]+1