# import sys
# sys.stdin = open('input.txt')

from collections import deque

# n,m=map(int,input().split())


# a =[ (idx,val) for idx,val in enumerate(list(map(int,input().split())))   ]


# a = deque(a) 

# # print(a) deque([(0, 60), (1, 50), (2, 70), (3, 80), (4, 90)])


# cnt = 0 
# while True:
#     cur = a.popleft() # (0,60)

#     if any(cur[1] < x[1] for x in a   ):  # 우선순위가 높은게 있다면 
#         a.append(cur)

#     else: # 우선순위가 높은 게 없다면  
#         # 위험도가 가장 높음
#         cnt+=1 
#         if cur[0] == m :            
#             break
# print(cnt) 





n,m = map(int,input().split())

a = [(i,v) for i,v in enumerate(list(map(int,input().split())))   ]

a = deque(a)
cnt = 0 
while True:
    # 일단 하나 뽑아
    x = a.popleft()
    
    if any( x[1] < i[1] for i in a   ) :
        # 우선순위가 0번 인덱스 값보다 큰경우 
        
        a.append(x)
    
    else: 
        # 뽑은애가 우선순위 큰경우 
        cnt+=1 
        if m == x[0] : 
            break
print(cnt)


