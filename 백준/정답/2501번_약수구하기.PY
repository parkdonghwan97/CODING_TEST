
a, b = map(int,input().split())
answer = []

for i in range(1, a+1): # 1~ 6
    if a % i == 0:
        # print(i)
        answer.append(i)

if len(answer)  <b:
    print(0)

else:
    print(answer[b-1])