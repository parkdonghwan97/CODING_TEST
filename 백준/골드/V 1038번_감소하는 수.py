
#처음 큐에 '0'~'0'까지 넣어두고
#하나씩 꺼내며 0~9까지 숫자를 하나씩 덧붙여보며 감소하는 수가 되는지 확인

# 감소하는수가 되면 tot+=1 ,  tot==n이녁ㅇ우 마지막들어간 숫자를 출력 후 종료

from collections import deque 

n = int(input())
q = deque(['0','1','2','3','4','5','6','7','8','9'])

tot = 9

if n <=9:
    print(q[n])
    exit()

while q :
    c = q.popleft()
    for i in range(0,10):
        if int(c[-1])  <= i :
            break
        q.append(c+str(i))
        tot+=1
        if tot ==n:
            print(q[-1])
            exit()
print(-1)


