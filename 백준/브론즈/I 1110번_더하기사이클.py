
'''
흰|검|흰|검|흰|검|흰|검
1 0 1 0 1 0 1 0
검|흰|검|흰|검|흰|검|흰
0 1 0 1 0 1 0 1


0,2,4,6


'''
board = [ 
    [1,0,1,0,1,0,1,0] ,
    [0,1,0,1,0,1,0,1] ,
    [1,0,1,0,1,0,1,0] ,
    [0,1,0,1,0,1,0,1] ,
    [1,0,1,0,1,0,1,0] ,
    [0,1,0,1,0,1,0,1] ,
    [1,0,1,0,1,0,1,0] ,
    [0,1,0,1,0,1,0,1] 
  ]

cnt=0
for i in range(8):
    a = input()
    for j in range(8):
        print(board[i][j], a[j])
        if board[i][j]==1 and a[j]=='F':
            cnt+=1
print(cnt)