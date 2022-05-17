# 17427 번 코드를 가져왔음.
# ㄴ> 전부 시간초과네..

# 시간초과 코드 
# def solve(x):
#     n = x
#     tot = 0 
#     for i in range(1,n+1):
#         tot += n//i * i 
#     return tot

# T = int(input())
# for i in range(T):
#     x = int(input())
#     print(solve(x))


#  다른 코드 O(n^2) 시간초과


# n = int(input())
# for i in range(n):
#     tot = 0
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             if i% j ==0:
#                 tot += j 
#     print(tot)

#  다른 코드 O(n root(n)) 시간초과
 
# n = int(input())
# for i in range(n):
#     tot = 0

#     for i in range(1, n + 1):
#         for j in range(1, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 tot += j
#                 if i // j != j:  # 예를 들어 i가 25일 경우 5가 두번 들어가는 것을 방지
#                     tot += (i // j)
#     print(tot)

'''
동적프로그래밍을 사용 시간복잡도 O(n log n)

배수의 원리를 이용하자.
1. n = ab 
2. a와 b는 n의 약수
3. n은 a와 b의 배수 

6 = 2*3 이므로 2와 3은 6의 약수이고  6또한 2, 3의 배수이다.
약수가 아닌 수는 연산하지 않으며 불필요한 연산을 줄일 수 있다.
N은 N의 약수의 배수로 이루어져 있기 때문에 DP 배열을 만들 수 있다.
미리 DP 배열을 만들어 놓고 그에 맞는 값을 입력받아 출력하면 됨

'''

# 최대값 설정
MAX=1000000

# DP 1로 초기화
dp = [1]*(MAX+1)

# S: 값 누적 리스트
s = [0]*(MAX+1)

for i in range(2, MAX+1):
    j=1
    while i*j <= MAX:
    	# i의 배수에 값 추가
        dp[i*j] += i
        j += 1

for i in range(1, MAX+1):
	# 누적 값 계산
    s[i] = s[i-1] + dp[i]

n = int(input())
ans=[]
for _ in range(n):
    a=int(input())
    ans.append(s[a])
print('\n'.join(map(str, ans))+'\n')
