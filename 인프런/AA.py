 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();

from itertools import combinations
n = int(input())

answer = [] 

for i in range(n):
    numbers = list(combinations(list(map(int,input().split())  ),3 ))
    score = 0 

    for num in numbers:
        tmp = sum(num)%10 
        score = max(tmp,score)
    answer.append( (score , i+1)  )

answer = sorted(answer, key= lambda x : (-x[0],-x[1]))
print(answer[0][1])


