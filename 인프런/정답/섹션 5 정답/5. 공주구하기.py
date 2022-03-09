# import sys
# sys.stdin = open('input.txt')



from collections import deque


n,k = map(int,input().split() )

a = []
for i in range(1,n+1):
    a.append(i)

dq =  deque(a) 
# print(dq)  deque([1, 2, 3, 4, 5, 6, 7, 8])

# ex) k = 3 
# 1 2 3 4 5 6 7 8 
#   2 3 4 5 6 7 8 1 
#     3 4 5 6 7 8 1 2 
#     x 4 5 6 7 8 1 2   --- 반복 

while len(dq) != 1 :
    for i in range(k-1):
        cur = dq.popleft() #   2 3 4 5 6 7 8
        dq.append(cur)     #   2 3 4 5 6 7 8 1 

    #  # k-1번 반복

    dq.popleft() # #     x 4 5 6 7 8 1 2 

# print(dq)   deque([7])
print(dq[0])