


# import sys
# sys.stdin=open("input.txt", "r")
# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 





# - 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# - 고른 수열은 오름차순이어야 한다

# ㄴ> 조합의 조건

from itertools import combinations

n , m = map(int,input().split())

arr = []
for i in range(n):
    arr.append(i+1)

# 위의 세줄을 arr  = [i+1 for i in range(n)] 이렇게 쓸 수 있음 

for i in combinations(arr,m):
    print( *i )