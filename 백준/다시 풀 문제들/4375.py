
'''

1로만 이루어진 N의 배수를 찾는다 > 1%N, 11%N, 111%N ... 수 중에서 길이가 최소인 값을 찾는 문제.

(A+B)%N=(A%N+B%N)%N
(A∗B)%N=(A%N)∗(B%N)%N
나머지는 성립하지 않음
(A−B)%N=((A%N)−(B%N)+N)%N
이런 꿀팁이 있었네.

# 이런 문제는 try except로 입력 오류날때 탈출하는 식으로 푸는건가
'''

while 1: 
    try:    
        n =int(input())
    except:
        break

num = 0
i = 1 
while 1:
    num = num*10 +1
    num %= n 

    if n==0:
        print(i)
        break
    i+=1