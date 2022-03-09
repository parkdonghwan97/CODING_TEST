# import sys  
# sys.stdin=open("input.txt","rt")

##  서칭해보고 푼 문제니 다시 풀어볼것.

import re


N, K = map(int,input().split())

X = list(map(int,input().split()))
answer=set()  # 중복 제거 
# X = X.sort(reverse=True)

for i in range(N):
    for j in range(i+1,N): # i+1번부터 n-1번 인덱스까지
        for l in range(j+1,N):
            answer.add( X[i]+X[j]+X[l] )

answer=list(answer)    
answer.sort(reverse=True)
print(list(answer)[K-1])


