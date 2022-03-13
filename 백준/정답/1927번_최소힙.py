


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();



import heapq as hq
import sys

n = int(input())
heap = []


for i in range(n):
    
    # x = int(input()) # 시간초과
    x = int(sys.stdin.readline())

    if x ==0:
        
        if len(heap) == 0 :
            print(0)
        else:
            print(hq.heappop(heap))
    
    else:
        hq.heappush(heap, x)

