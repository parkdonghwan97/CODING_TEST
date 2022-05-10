 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();




n = int(input()) # 시험장
a = list(map(int,input().split()) )  # 응시자
b,c = map(int,input().split()) # 감독관


cnt = n 
for i in a :
    i-=b 
    if i>0:

        if i % c :
            cnt+= (i//c) + 1 
        else:
            cnt += (i//c )

print(cnt)
