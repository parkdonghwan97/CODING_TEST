# import sys
# sys.stdin = open('input.txt')

'''
5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2
'''
n = int(input())
a = list()
for i in range(n):
    a.append(list(map(int,input().split())))
# 맨앞,뒤에 n+ 2만큼 추가 
a.insert(0,[0]*(n+2))
a.insert(n+1,[0]*(n+2))              
# a.extend([0]*(n+2))

# 맨 앞, 뒤위 0 배열 빼고 나머지 리스트들 앞뒤로 0 추가
for i in range(1, len(a)-1): 
    a[i].insert(0,0)
    a[i].insert(n+1,0)
# print(a) [[0, 0, 0, 0, 0, 0, 0], [0, 5, 3, 7, 2, 3, 0], [0, 3, 7, 1, 6, 1, 0], [0, 7, 2, 5, 3, 4, 0], [0, 4, 3, 6, 4, 1, 0], [0, 8, 7, 3, 5, 2, 0], [0, 0, 0, 0, 0, 0, 0]]

cnt = 0 # 봉우리 개수 
for i in range(1, n+1):
    for j in range(1,n+1):  # 입력한 변수의 인덱스 값이 상하좌우보다 크면 cnt에 더함 
        if a[i][j] > a[i-1][j] and a[i][j] > a[i+1][j]and a[i][j] > a[i][j-1]and a[i][j] > a[i][j+1]:
            cnt += 1

print(cnt)   







