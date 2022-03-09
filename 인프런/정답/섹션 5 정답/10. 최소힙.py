# import sys
# sys.stdin = open('input.txt')

import heapq as hq

# a = []  
# while True:
#     n = int(input())
#     if n == -1 :      # -1 입력시 종료
#         break
    
#     if n== 0 :    # 0 입력시 힙에서 가장 root노드 print()

#         if len(a) == 0 : # a가 비어있는경우 -1 출력 
#             print(-1)

#         else:  # a가 비어있지 않으면
#             print(hq.heappop(a))    # root 노트 pop 

    

#     else:   # 0이 아닌경우 push
#         hq.heappushpop(a, n) # a의 리스트에 n 값을 최소 힙으로 넣음 

a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)


