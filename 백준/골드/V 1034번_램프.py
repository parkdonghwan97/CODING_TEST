
#  (0의 개수가 K보다 작거나 같고), 
# (K가 짝수면 0의 개수도 짝수,K가 홀수면 0의 개수도 홀수)



'''
0의 개수가 스위치를 누르는 횟수인 K보다 많으면 절대로 꺼져있는 램프들을 다 못켬. 
0의 개수가 1개인데 K가 2일 경우 어떤 스위치를 2번 누르던 행을 모두 킬 수 없다.
(0의 개수 <= K의 개수) and (0의 개수%2 == K%2)를 만족하는 행만 행에 있는 모든 램프를 킬 수 있다.

한 행의 모든 램프를 킬 수 있다면, 이 행과 똑같이 생긴 다른 행도 킬 수 있으므로 똑같은 값을 가진 행들의 개수를 구함
모든 행에 대해 반복하면서 어떤 행을 모두 킬 수 있다면 그 행과 똑같은 값을 가진 행의 개수들을 세고 센 값들 중 최대값을 구하면 정답이다.
'''
# n,m = map(int,input().split()) # n행 m열
# arr = [input() for i in range(n)]  
# k = int(input())

# cnt = [0] * n

# if k % 2 :
#     for i in range(n):
#         zero_cnt = arr[i].count('0')

#         if zero_cnt % 2 and zero_cnt <= k :
#             for j in range(n):
#                 if arr[i] == arr[j]:
#                     cnt[i]+=1
# else:
#     for i in range(n):
#         zero_cnt = arr[i].count('0')
#         if not zero_cnt %2 and zero_cnt <=k:
#             for j in range(n):
#                 if arr[i] == arr[j]:
#                     cnt[i]+=1
# print(max(cnt))

# 방법2
n,m = map(int,input().split())
board = [] 
for i in range(n):
    board.append(list(map(int,input())))
k = int(input())
answer = 0 

for i in range(n):
    cnt = board[i].count(0)
    cnt2 = 0 
    if cnt <=k and ((cnt%2)==(k%2)):
        for j in range(n):
            if board[i] ==board[j]:
                cnt2+=1
    answer = max(answer, cnt2)
print(answer)

