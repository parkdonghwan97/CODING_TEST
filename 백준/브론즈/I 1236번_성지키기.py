
# N 세로, M 가로


# M,N = map(int,input().split())


# castle = []

# for i in range(M):
#     castle.append(input())


# r =0
# c= 0

# for i in range(M):
#     if 'X' not in castle[i]:
#         r+=1

# for j in range(N):
#     if 'X' not in [castle[i][j] for i in range(M)]:
#         c+=1
# print(max(c,r))

# 다른사람 코드
n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(input())

row = [0] * n
col = [0] * m


for i in range(n):
    for j in range(m):
        if array[i][j] == "X" :
            row[i] = 1
            col[j] = 1

row_count = 0
for i in range(n):
    if row[i] == 0:
        row_count += 1
col_count = 0

for i in range(m):
    if col[i] == 0:
        col_count += 1
        
print(max(row_count, col_count))