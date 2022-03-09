from ntpath import join
import sys
# import sys
# sys.stdin=open("input.txt", "r")
# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 



n = int(input())
answer= []
for i in range(n):
    x,y = map(int,input().split())
    answer.append( [x,y] )

answer.sort( key = lambda v : (v[0] ,v[1]))


# for i in answer:
#     print(i, end= ' ')

for i in range(len(answer)):

    print(*answer[i])