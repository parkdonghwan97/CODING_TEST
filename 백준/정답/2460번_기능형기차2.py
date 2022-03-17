
answer = 0
x = [] 
for _ in range(10):
    o,i = map(int,input().split())
    answer = answer + i-o
    x.append(answer)
print(max(x))

