


# 시간초과,,,

# def cal(x):
#     global answer
#     for i in range(1,x+1):
#         if x % i == 0:
#             answer += i 
    
#     return
# N = int(input())

# x = 0
# answer = 0
# for i in range(1,N+1):
#     cal(i)

# print(answer)

n = int(input())
tot = 0 
for i in range(1,n+1):

    # 1부터 n 범위 내에서 i의 배수의 개수 = 1 부터 n의 범위내에 i를 약수로 가지는 개수(n을 i로 나눈 몫)
    # 예를 들면 1부터 100까지 11의 배수의 개수는 11, 22 33 ---99 9개= 100//11 
    tot += n//i * i 
print(tot)


#  다른 코드 O(n^2)

n = int(input())
tot = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        if i% j ==0:
            tot += j 
print(tot)

#  다른 코드 O(n root(n))

n = int(input())

sum_ = 0

for i in range(1, n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            sum_ += j
            if i // j != j:  # 예를 들어 i가 25일 경우 5가 두번 들어가는 것을 방지
                sum_ += (i // j)
print(sum_)