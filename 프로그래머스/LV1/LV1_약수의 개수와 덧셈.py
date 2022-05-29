# LV1 약수의 개수와 덧셈

# 약수의 개수 구하는 함수
def sol(x):
    cnt = 0
    for i in range(1,x+1):
        if x % i == 0:
            cnt+=1
    return cnt 
        
        
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if sol(i) % 2 ==0   :   # 짝수인 경우 더함
            answer += i
        else:
            answer -=i
    
    return answer
# 다른 사람 코드

# 제곱수의 약수는 홀수임. 
def solution(left, right):
    answer = 0
   
    return sum([-n if int(n ** 0.5) == n ** 0.5 else n for n in range(left, right+1)])   # 이렇게 한줄 코딩이 가능하구나 
