# import sys
# sys.stdin = open('input.txt')

a = list()
for i in range(9):
    a.append(list(map(int,input().split())))


# 음 일단 1차원적으로 행별로, 열별로 1~9까지 있는지 확인 + 특정 인덱스의 값을 기준으로 8방향의 값들이 1~9인지

# 음 1~9까지 있는지 확인하는 방법이 뭐가있을까?  => 합이45   
Flag = "NO"
for i in range(len(a)):
    tot1 = 0 
    tot2 = 0
    for j in range(len(a)):
        tot1+= a[i][j]   # 행의 합 
        tot2+= a[j][i]   # 열의 합이 모두 45인경우  
    if tot1 ==45 and tot2 ==45:
        Flag  = "YES"  
'''       
인덱스가 
[1][1] ,[4][1], [7][1]
[1][4] ,[4][4], [7][4]  이 녀석들만  상하좌우값 45인지 확인하면 될거같은데 코드가 갱장히 더러울것으로 예상...
[1][7] ,[4][7], [7][7]  
'''
for i in range(1,8,3):
    for j in range(1,8,3):
        if a[i-1][j-1] + a[i-1][j]+a[i-1][j+1] + a[i][j-1] +a[i][j] + a[i][j+1] + a[i+1][j-1] + a[i+1][j]+a[i+1][j+1] == 45:
            Flag = 'YES'
        else:
            Flag = 'NO'
print(Flag)

    

