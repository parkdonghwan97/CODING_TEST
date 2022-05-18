

# I 1296번_팀 이름 정하기

'''
L = 연두의 이름과 팀 이름에서 등장하는 L의 개수
O = 연두의 이름과 팀 이름에서 등장하는 O의 개수
V = 연두의 이름과 팀 이름에서 등장하는 V의 개수
E = 연두의 이름과 팀 이름에서 등장하는 E의 개수

우승확률
((L+O) × (L+V) × (L+E) × (O+V) × (O+E) × (V+E)) mod 100
'''

# 내코드 실패; 이렇게 푸는거 아님 문제 다시 읽을 것

# from itertools import combinations
# def love(x):
#     global a 
#     alist = list(a)
#     tmp = []
#     for i in a:
#         tmp.append(x.count(i))
#     print(tmp)
#     c = combinations(tmp,2)
#     tmp2 = []
#     for i in c:
#         tmp2.append(sum(i))
#     x=1
#     print(tmp2)
#     for i in tmp2:
#         x *= i
#     x = x % 100
   
#     return x



# a = input()
# n = int(input())
# namelist = []
# answer = []
# for i in range(n):
#     namelist.append(input())

# for i in namelist:
#     print(love(i))

# 다른 사람 코드 
# 아니 이거 문제가 이상한거같은데 
# 왜 LOVE로 고정된건지
# import sys

# def solution() :
#     y = sys.stdin.readline().rstrip()
#     n = int(sys.stdin.readline())
#     std = list('LOVE')
    
#     if n == 1 :
#         print(sys.stdin.readline().rstrip())
#     else :
#         res = []
#         for _ in range(n) :
#             s = sys.stdin.readline().rstrip()
                
#             calc = 1
#             for i in range(len(std)) :
#                 for j in range(i+1, len(std)) :
#                     calc *= (y.count(std[i]) + s.count(std[i])) + (y.count(std[j]) + s.count(std[j]))
            
#             res.append((calc % 100, s))
        
#         res.sort(key = lambda x : (-x[0], x[1]))

#         print(res[0][1])
                                 
# solution()


Y = list(map(str,input()))
N = int(input())
score = {}
for i in range(N):
    Name = input()
    TN = list(map(str, Name))
    F = Y + TN
    L = F.count('L')
    O = F.count('O')
    V = F.count('V')
    E = F.count('E')
    score.update({Name : (((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100)})
# score = sorted(score.items())
# print(score)
score = dict(sorted(score.items()   )) 
print(max(score, key= score.get))