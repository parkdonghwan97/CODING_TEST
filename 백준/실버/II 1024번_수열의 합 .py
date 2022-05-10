

# N,L= map(int,input().split()) # 18 2 

'''
이건 수학적 풀이가 필요해서 25%밖에 안되는 것 같다.
N = (X+1)+(X+2)+(X+3)+...+(X+L)
N = Lx + L(L+1) / 2 
Lx = N - L(L+1) / 2

# 음이 아닌 정수이기 때문에  L+1은 0보다 큼.

L부터 100까지 확인해보며 x를 구하고  못구하면 -1
'''

# for i in range(L,101):  # 2부터 101
    
#     x = N - (i (i + 1) / 2)   
#     if x % i == 0:         
#         x = int(x/i)        

#         if x >= -1 :                
#             for j in range(1, i+1): 
#                 print(x+j, end=' ')
#             print()
#             break
# else:
#     print(-1)


# 방법 2
'''
N = LX+(1+2+3+...+L+1)
N = LX+L(L-1)/2

X = N/L - (L-1)/2
'''



N, L = map(int,input().split())
 
answer = -1
while True:
    if L > 100:
        break
    temp = N/L-(L-1)/2
    if temp < 0:
        L+=1
        continue
    if int(temp) == temp:
        answer = int(temp)
        break
    L+=1
if answer >= 0:
    print(*range(answer,answer+L))
else:
    print(-1)