from ntpath import join
import sys
# import sys
# sys.stdin=open("input.txt", "r")
# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 



n = int(input())

answer=[]
for i in range(n):
    name, kor, eng, math = map(str, input().split() ) 
    answer.append((name, int(kor), int(eng), int(math) ))
    

# print(answer)

# 국어 내림차순, 영어 오름차순, 수학 내림차순, 이름 오름차순 

answer.sort(key = lambda v :  ( -v[1], v[2], -v[3], v[0]  )     )


for i in answer:
    print(i[0])