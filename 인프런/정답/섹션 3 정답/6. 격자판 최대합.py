# import sys
# sys.stdin = open('input.txt')
# 3-6번

n = int(input())
M = []
for i in range(n):
    m = list(map(int,input().split()))
    M.append(m)
# print(M) [[10, 13, 10, 12, 15], [12, 39, 30, 23, 11], [11, 25, 50, 53, 15], [19, 27, 29, 37, 27], [19, 13, 30, 13, 19]]

# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

tot = []
sum3 = 0    # 대각선 합1
sum4 = 0    # 대각선 합2 
for i in range(n):
    sumv = 0    # 가로합
    sumh = 0    # 세로합
    
    for j in range(n):
        sumv += M[i][j]
        sumh += M[j][i]
    # 1행합, 1열합 더함    
    tot.append(sumh) 
    tot.append(sumv)
# 대각선 합 더하기   M[0][0], M[1][1], M[2][2],,,,,M[4][4] /////   M[0][4], M[1][3],,,,M[4][0]
    sum3 += M[i][i]
    sum4 += M[i][n-1-i]
tot.append(sum3)
tot.append(sum4)
print(max(tot))
# print(tot)
