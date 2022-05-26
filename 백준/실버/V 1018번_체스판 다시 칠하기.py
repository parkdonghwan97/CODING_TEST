

# V 1018번_체스판 다시 칠하기
'''
1. w로 시작하는 경우
2. b로 시작하는 경우
'''



n,m = map(int,input().split())

start_W = [[0] * m for i in range(n) ]
start_B = [[0] * m for i in range(n) ]
cnt = float('inf')
arr = []
for i in range(n):
    arr.append(list(input()))

for i in range(n):
    for j in range(m):
        if not (i+j) % 2 :
            start_W[i][j] = 'W'
            start_B[i][j] = 'B'
        else:
            start_W[i][j] = 'B'
            start_B[i][j] = 'W'
for i in range(n-7):
    for j in range(m-7):
        tmp_W,tmp_B = 0,0
        for x in range(8):
            for y in range(8):
                if arr[i+x][j+y] != start_W[i+x][j+y]:
                    tmp_W +=1
                if arr[i+x][j+y] != start_B[i+x][j+y]:
                    tmp_B +=1
        cnt = min(cnt,tmp_B)
        cnt = min(cnt,tmp_W)
print(cnt)         
