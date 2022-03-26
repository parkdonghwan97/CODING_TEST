 


# import sys
# sys.stdin=open("input.txt", "r")

# input = sys.stdin.readline       # 입력 량이 많을 때 사용. 
# s = intput().rstirp();

# 세사람 값이 다르다.
def DFS(L):
    global x
    if L == n:
        # answer = set(answer)
        
        if max(answer) - min(answer) < x :
            tmp = set()

            for i in answer:
                # answer.add(i)
                tmp.add(i)
            if len(tmp) == 3:
                x   =  max(answer) - min(answer)
                

    else:
        for i in range(3):  # 3 명 
            answer[i] += coin[L]
            DFS(L+1)
            answer[i] -= coin[L] #  back할때 다시 빼줌
             

coin = []
n = int(input())
for i in range(n):
    k = int(input())
    coin.append(k)
answer = [0] *3
x = 9999
DFS(0)

print(x)