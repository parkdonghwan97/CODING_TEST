

# 수퍼바이러스
import sys

K,P,N = map(int,sys.stdin.readline().rstrip().split())

'''


처음 K 
1초당  P배씩 증가 
N초 후에는?
'''

# for i in range(N):
#     K = K * P
# print(K%1000000007)

# 시간 초과

# 방법 2 
for i in range(N):
    K = (K * P)%1000000007
print(K)


# 방법 3
#  pow(base, exp, mod)를 이용 해야한다.
# print((K * pow(p, n, 1000000007)) % 1000000007)