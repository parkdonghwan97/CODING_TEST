# import sys
# sys.stdin = open('input.txt')

n = int(input())
a = []
for i in range(n):
    cm, kg = map(int,input().split())
    a.append( (cm,kg) )

#  키순 내림차순 정렬
a.sort(reverse=True)
largest = 0 
cnt = 0 
for cm, kg in a :
    if kg > largest:
        cnt+=1
        largest = kg 
print(cnt)


