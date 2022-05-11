#  해당 코드는 시간초과 오류가뜸.
# DP를 사용해야함 
# 배열을 사용할 경우 시간을 단축시킬 수 있음

# def fibo(x):
#     global cnt0,cnt1
#     if x == 0:
#         cnt0+=1
#         return 0
#     elif x==1:
#         cnt1 +=1
#         return 1
#     else:
#         return fibo(x-1) + fibo(x-2)



# T = int(input())

# for i in range(T):
#     cnt0,cnt1 = 0,0
#     n = int(input())
#     fibo(n)
#     print(cnt0, cnt1)


# 시간초과 문제를 해결하기 위해 0과 1의 규칙을 찾아 해결
# 0의 개수 = 이전 1의 개수
# 1의 개수 = 이전 0 +이전 1의 개수

T =int(input())

for i in range(T):
    cnt0=[1,0]
    cnt1=[0,1]
    n = int(input())
    print(cnt0[-2])

    if n>1:
        for j in range(n-1):
            cnt0.append(cnt1[-1])
            cnt1.append(cnt0[-2]+cnt1[-1])
    print(cnt0[n],cnt1[n])