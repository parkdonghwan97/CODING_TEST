

import sys
# import sys
# sys.stdin=open("input.txt", "r")
# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 

import math
n = int(input())

for i in range(n):
    arr= list(map(int,input().split()))

    cnt = 0 

    for j in range(1,len(arr)):
        for k in range(j+1, len(arr)):
            cnt += math.gcd(arr[j] , arr[k]  )

    print(cnt)