

# V 1531번_투명  
# 처음에 100 * 100을 받았는데 인덱스 오류가 떠서 하는수없이 101 *101을 했음
n,m = map(int,input().split())
board = [[0]* 101 for i in range(101)   ]

for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())

    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            board[i][j]+=1

cnt = 0 
for i in range(101):
    for j in range(101):
        if board[i][j] > m :
            cnt+=1
print(cnt)

# 다른사람 풀이
n,m= map(int,input().split())
board = [[0]*100 for x in range(100)]
for k in range(n):
    xi, yi, xf, yf = map(int, input().split())
    for i in range(xi, xf+1):
        for j in range(yi, yf+1):
            board[i-1][j-1] += 1               # 여기서 문제가 있었네  i 와 j 에서 1씩 뺀 인덱스에 1을 더해야했다.
count = 0
for i in range(100):
    for j in range(100):
        if board[i][j] > m:
            count += 1
print(count)